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
    

Running the docker
    docker run -it test:pandas

Sending parameters to docker
    docker run -t test:pandas arg2
    The entry point in the dockerfile should be capable to handle the argument