# DDM AC 05

It's are using the WAASD (Worker as aplication server designe).

Navigate `src/main` to see the business login and see `src/application_server` see the server and application configuration.

Just respect layear main responsability.

## Installing the dependencies

run `pipenv install` to install all dependencies.


## Starting the DB

Until now, just start the DB using the docker-compose, run `docker-compose up db` to starts the MySQL Database.


## Migrations

Don't forget about run migrations, just run `python src/run_migrations.py`.

## Starting the project

Run `python src/__main__.py` to starts the project.
