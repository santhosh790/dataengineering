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