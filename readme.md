# Parser

## Instalation
to run this project your need to install PostgreSQL and download chromedriver for your chrome version
after you clone project you need to make this commands:
##
create virtual enviroment:
```bash
python3 -m venv venv
```
##
activate virtual enviroment:
```bash
. venv/bin/activate
```
##
install required modules:
```bash
pip install -r requirments.txt
```
##create .env file:
```bash
touch .env
```

fill .env file with:
DB_NAME=
DB_USER=
USER_PASSWORD=
HOST=localhost
PORT=5432
DRIVER_PATH=
URL=https://www.kijiji.ca/b-apartments-condos/city-of-toronto/c37l1700273

insert your values to DB_NAME, DB_USER, USER_PASSWORD, DRIVER_PATH

run parser_.py file to start parser







