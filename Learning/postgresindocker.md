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

Issue encountered and solved:
1. ImportError "no pq wrapper available" when installing pgcli.
    Had to install another package called *pip install "psycopg[binary,pool]"* to solve this.
2. "psql: could not connect to server: Connection refused" Error when connecting to remote database
    This one was mainly because the server is not picking the proper port.
    Just goto *postgresql.conf* and edit the port in the file. This solves the issue.


