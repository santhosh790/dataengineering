Pandas
----

    Reading a parquet file:
        pd.read_parquet('<filename>.parquet')
    Read as chunks:
        pd.read_csv('<filename>.csv', iterator=True, chunksize=10000)
    Drop a column
        df.drop('colname', axis=1, inPlace=True)
    
ArgParse
-----
    https://docs.python.org/3/library/argparse.html

Main Block
-----

    https://docs.python.org/3/library/__main__.html


Simple HTTP Server at a folder:

    python -m http.server



python3 ingestion_script.py \
    --user=root \
    --password=test \
    --host=localhost \
    --port=7001 \
    --dbname=ny_taxi \
    --table_name=yellow_taxi \
    --url=https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2022-01.parquet

https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2022-01.parquet
python3 ingestion_script.py \
    user=root \
    password=test \
    host=localhost \
    port=7001 \
    dbname=ny_taxi \
    table_name=yellow_taxi \
    url="https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2022-01.parquet"


python3 ingestion_script.py root test localhost 7001 ny_taxi yellow_taxi "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2022-01.parquet"

docker run -it ingest_taxt:v001 root test localhost 7001 ny_taxi yellow_taxi "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2022-01.parquet"