Jupyter Notebook

Installing jupyter notebook:
    
    pip install jupyter

starting it from console:

    jupyter notebook

Understand the Python executable [Kernal] at which the jupyter notebook is running:

        import sys
        sys.executable

Add Kernel in existing python:

pip install ipykernel

python -m ipykernel install --user --name myenv --display-name "Python (myenv)"

Converting the notebook into a script file:

    jupyter nbconvert --to=script <filename>.ipynb

This will create a python script file with <filename>.py

docker run -it \
    -e POSTGRES_USER="root" \
    -e POSTGRES_PASSWORD="test" \
    -e POSTGRES_DB="ny_taxi" \
    -v /Users/a616152/Documents/Personal/DataEngineering/Learning/ny_taxi/data:/var/lib/postgresql/data \
    -p 7001:7001 \
    postgres:13