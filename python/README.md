# Python language

This project implements 2 endpoints:
1. /api/hello returns hello world
1. /api/content CRUD implementation
    1. POST /api/create_content CREATE resource Body: {"color": "#ffffff", "title": "white"}
    1. GET and POST /api/read_content?id=1 READ resource
    1. POST /api/update_content?id=1 UPDATE resource Body: {"color": "#ffffff", "title": "white"}
    1. POST /api/delete_content?id=1 DELETE resource

## Install

- Have the latest Python 3 installed [Download](https://www.python.org/)
- Have a running Postgres database all setup
- Create a .env file. Fill DATABASE_URL with connection string
- Create a virtual env (optional)
- Download dependencies 
```sh
pip install -r requirements.txt
```
- Have Azure Core Tools installed
- Running locally:
```sh
func start
```

##

## Details
- ORM: [SqlAlchemy](https://www.sqlalchemy.org/)
