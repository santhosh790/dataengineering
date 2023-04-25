PostGres
-- 
// Repeat from dockerlearning page for continuity
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
    -p 7001:7001 \
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
// Repeat from dockerlearning page

pgcli commands:
https://www.pgcli.com/commands



Issue encountered and solved:
1. ImportError "no pq wrapper available" when installing pgcli.
    Had to install another package called *pip install "psycopg[binary,pool]"* to solve this.
2. "psql: could not connect to server: Connection refused" Error when connecting to remote database
    This one was mainly because the server is not picking the proper port.
    Just goto *postgresql.conf* and edit the port in the file. This solves the issue.

_____

pgAdmin
-- 

it is a webbased GUI tool for PostgreSql.

Running pgAdmin container using docker hub - https://hub.docker.com/r/dpage/pgadmin4/

Get docker image of pgAdmin container

    docker pull dpage/pgadmin4

Running it in docker:

    docker run -it \
        -e PGADMIN_DEFAULT_EMAIL='admin@admin.com' \
        -e PGADMIN_DEFAULT_PASSWORD='root' \
        -p 8080:80 \
        dpage/pgadmin4


Inorder to connect postgres server using pgAdmin, we need to make them available in same network. so, both can be connected. To do this, we need to use docker network. Once network created, use network name to run postgres server and pgadmin.

    docker run -it     -e POSTGRES_USER="root"     -e POSTGRES_PASSWORD="test"     -e POSTGRES_DB="ny_taxi"     -v /Users/a616152/Documents/Personal/DataEngineering/Learning/ny_taxi/data:/var/lib/postgresql/data     -p 7001:7001  --network=pg-network --name=pg-db   postgres:13

After running this, we can validate the existing db is available using pgcli.


    docker run -it -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" -e PGADMIN_DEFAULT_PASSWORD="root" -p 8080:80 --network=pg-network --name=pg-admin dpage/pgadmin4


Once pgAdmin started, provide postgres server credentials and see if we are able to see the database and table.

The ingestion script need to be created as docker file, the command to create is in dockerlearning.md.

After creation, we need to run the this ingestion script container using pg-network as network as the postgres is under it.

    docker run -it --network=pg-network ingest_taxt:v001 root test pg-db 7001 ny_taxi yellow_taxi "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2022-01.parquet"
