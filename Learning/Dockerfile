FROM python:3.9

RUN pip install pandas

WORKDIR /apps
COPY pipelinefile.py pipeline.py

#ENTRYPOINT ["bash"] Entry point can be of any number of values. We need to properly set by seeing wat it is going to take
ENTRYPOINT ["python", "pipeline.py"]