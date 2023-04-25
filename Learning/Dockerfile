FROM python:3.9

RUN apt-get install wget
RUN pip install pandas sqlalchemy psycopg2 fastparquet 

WORKDIR /apps
COPY ingestion_script.py ingest_pipeline.py

#ENTRYPOINT ["bash"] Entry point can be of any number of values. We need to properly set by seeing wat it is going to take
ENTRYPOINT ["python", "ingest_pipeline.py"]