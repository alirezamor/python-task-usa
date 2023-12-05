# Explanation
I've decided to use relational database, because I think that there would be another tables which needs to be related
to the existing table. I can also non-relational databases like MongoDB and it's so easier to handle the search staff.
I have two tables Users and Tasks. They include the fields which are mentioned in the task. I've also provided crud 
endpoints and also search endpoint. The reason that I haven't implemented pagination file, exceptions and utils is that
I've found you just want the database architecture. You can also check the tables' columns in alembic revisions. 

# Running application
## Application requirements
1. Python 3.11+
2. Virtualenv
3. Postgresql


## Enabling gin in postgres

To enable gin indexing in postgresql you have to execute the commands below in a query tool which connected to
your postgresql DB:

```SQL
CREATE EXTENSION pg_trgm;
CREATE EXTENSION btree_gin;
```

## Migration
Before execute the migration you have to put your database connection info in line 63 in `alembic.ini` like below:
```ini
sqlalchemy.url = postgresql://postgres_username:postgres_password@postgres_host/postgres_db_name
```

Now you can execute migrations:
```shell
alembic upgrade head
```


## Populate User table in database
```SQL
INSERT INTO shirley.user (username, email) VALUES ('alireza', 'alireza.mor2012@gmail.com');
```

## Run The Application
First of all you have to define some environment variable for the database connection as below:
```shell
DB_USER=postgres_username
DB_PASSWORD=postgres_password
DB_HOST=postgres_host
DB_NAME=postgres_db_name
```
You can run the below command to run the application:
```shell
uvicorn src.main:app --host 127.0.0.1 --port 8000
```

## Remained Works
I have to add exception handling to the code and also log management. I want to create singleton object for log management.
I also wanted to add docker-compose file.
