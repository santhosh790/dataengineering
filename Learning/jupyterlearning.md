Jupyter Notebook

Installing jupyter notebook:
    
    pip install jupyter

starting it from console:

    jupyter notebook



docker run -it \
    -e POSTGRES_USER="root" \
    -e POSTGRES_PASSWORD="test" \
    -e POSTGRES_DB="ny_taxi" \
    -v /Users/a616152/Documents/Personal/DataEngineering/Learning/ny_taxi/data:/var/lib/postgresql/data \
    -p 7001:7001 \
    postgres:13