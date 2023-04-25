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


Easy Tricks
-----

1. Simple HTTP Server at a folder:

        python -m http.server
