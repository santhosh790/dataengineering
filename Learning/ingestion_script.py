import pandas as pd
import sys
from sqlalchemy import create_engine
from time import time
import argparse
import os
#import wget

def ingest_data(params):

    user = params.user
    password = params.password
    host = params.host
    port = params.port
    dbname = params.db
    table_name = params.table
    url = params.url
    filename = 'yellow_tripdata_2022-01.parquet'
    csv_file = 'yellow_trips.csv'


    print("User is "+user)
    print("pwd is "+password)
    print("db is "+dbname)
    print("Url is "+url )
    #download parquet file
    os.system(f"wget {url} -O {filename}")
    #wget.download(url, filename) - This was throwing ssl handshake issue.
    

    df = pd.read_parquet(filename)
    df.to_csv(csv_file)

    df_iter = pd.read_csv(csv_file, iterator=True, chunksize=10000)

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{dbname}')
    engine.connect()

    while True:
        t_start = time()
        
        df = next(df_iter)
        pd.to_datetime(df.tpep_pickup_datetime)
        pd.to_datetime(df.tpep_dropoff_datetime)
        
        df.drop('Unnamed: 0',axis=1, inplace=True)
        
        df.to_sql(name=table_name, con=engine, if_exists='append')
        
        t_end = time()
        
        print("Adding new chunk.. Took %.3f time" % (t_end-t_start))






if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Ingest Taxi data into PostGres')

    # params - username, pwd, host, port, dbname, tablename

    parser.add_argument('user',
                        help='username for the postgres')
    parser.add_argument('password',
                        help='pwd for the postgres')
    parser.add_argument('host',
                        help='hostname for the postgres')
    parser.add_argument('port',
                        help='port for the postgres')
    parser.add_argument('db',
                        help='databasename for the postgres')
    parser.add_argument('table',
                        help='Table name where the data posted')
    parser.add_argument('url',
                        help='Parquet file URL')

    args = parser.parse_args()
    print(args.user)
    #print(args['user'])
    ingest_data(args)

