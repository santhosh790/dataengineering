About:
-
It builds and runs the so called containers - an isolated image that runs specific task in a particular setting/environment independent of the settings/environment of the underlying OS. So, it is called OS-level virtualisation tool. Docker Engine hosts these containers.

Docker can be easily installed using the Docker Desktop (used to easily manage the docker in a GUI based system under a machine). 

Docker Desktop Download path: https://docs.docker.com/desktop/install/mac-install/

After installing check:
    docker --version
		Docker version 20.10.17, build 100c701
		
Run a simple docker image or container

	docker run hello-world

	output:
	Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (arm64v8)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
	
	$ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/


Starting Docker Desktop from prompt:
	open -a Docker

 -it - interactive mode (if not set, it will just run the image in background and come out)

To set entry point

    --entrypoint=bash
    it sets entrypoint as bash


Creating a docker file
-
Create a file with the name 'Dockerfile' or any name. 'Dockerfile' is default name.
Various docker commands can be used to write one. For example:
    	FROM python:3.9 - From the image 

        RUN pip install pandas - run this command

        ENTRYPOINT ["bash"]  - set this interactive endpoint
Building docker
-
    docker build -t test:pandas .
here,
  test - docker image name
  pandas - tag name
  . - place where it is stored

If you face any issue and wanted to see more info, run:
	DOCKER_BUILDKIT=0 docker build -t test:pandas .
    
Running the docker:
	docker run -it test:pandas

Sending parameters to docker
    docker run -t test:pandas arg2
The entry point in the dockerfile should be capable to handle the argument

docker ps 
    ps - present running services


Stopping a docker container:

    docker stop <container-id>

container-id can be found when we run "docker ps" command.

To list down local images:

        docker image ls

PostGres
-- 

Running a postgres image:

    docker run -it postgres:13

Below information required for POSTGres to work:
1. various environment variables need to be set for the postgres to run. [User, Password and DB name]
    -e - environmental variable
2. volumes -v 
    To say present working directory. You can say ${pwd}
3. Port  -p
4. Healthcheck


In case of ny taxi project, I'd set it like this:
    docker run -it \
    -e POSTGRES_USER="root" \
    -e POSTGRES_PASSWORD="test" \
    -e POSTGRES_DB="ny_taxi" \
    -v ${pwd}/ny_taxi/data:/var/lib/postgresql/data \
    -p 5432:5432 \
    postgres:13

Client to be used to access the database. A CLI client can be used. *pgcli* is one of it.
    
    pip install pgcli

Things to be specified for the CLI to connect
    -h - host
    -p - port
    -u - user
    -d - database name
In our case, it will look like this:
    
    pgcli -h localhost -p 5432 -u root -d ny_taxi

it can prompt for password.

In current case, it is now accessing the postgres database that got created from the image.




	docker run -t test:pandas arg2
The entry point in the dockerfile should be capable to handle the argument


Docker Network
====
 
 To let more than one docker containers to interact, we need to put those in same network. This docker network helps to facilitate the same. Reference: https://docs.docker.com/engine/reference/commandline/network_create/

    docker network create [OPTIONS] NETWORK

in our case, just

    docker network create pg-network

After creating the network, we need to specify this network name as and when we start or run the docker containers. 

Building ingestion docker:

        docker build -t ingest_taxt:v001 .


When mentioning the localhost url, it is known that docker container will not have access to the other container. We used docker network to solve this issue.

As pg-network is used in postgres server container's network:

    docker run -it --network=pg-network ingest_taxt:v001 root test pg-db 7001 ny_taxi yellow_taxi "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2022-01.parquet"

Docker Compose
====
Compose is a tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application’s services. Then, with a single command, you create and start all the services from your configuration. [https://docs.docker.com/compose/]

In simple terms, Compose helps it to possible for different containers work and interact together. So, Compose is a go-to tool during multi-container orchestration. The configuration files like yaml makes it easier to maintain the environmental variables.

Compose v1 was written in Python and more robust Compose v2 is written in Go. 

There are various ways to set environment variables: https://docs.docker.com/compose/environment-variables/set-environment-variables/

We can also utilize the profiling to let services take up extra params or add new services. E.g., For an application which has Frontend, Backend and DB, pgAdmin can run only when you want to see what is in DB. i.e., only for debug scenario. Profiling will be handy at these situations: https://docs.docker.com/compose/profiles/

    Installation
        Docker compose is already part of Docker Desktop. 
        or to install manually, follow: https://docs.docker.com/compose/install/

Getting Started
--
        https://docs.docker.com/compose/gettingstarted/
Steps:
    1. Create application with dependencies
    2. Create Docker file to create docker image
    3. Define services in docker compose file:
        As we already have done step 1 and 2, going to step 3. Create file called docker-compose.yml
    4. Build, run the app created at step 3.
       
            docker compose up
        To run it in detached mode:
            docker compose up -d

        To stop the compose:
            docker compose down

Note: docker-compose command is from Compose v1 and docker compose implies we use Compose v2.
        
