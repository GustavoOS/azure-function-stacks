# Go language

This project implements 2 endpoints:
1. /api/hello returns hello world
1. /api/content CRUD implementation
    1. POST /api/content CREATE resource Body: {"color": "#ffffff", "title": "white"}
    1. GET /api/content?id=1 READ resource
    1. PUT /api/content?id=1 UPDATE resource Body: {"color": "#ffffff", "title": "white"}
    1. DELETE /api/content?id=1 DELETE resource

## Install

- Have Go installed [Download](https://go.dev/)
- Have a running Postgres database all setup
- Create a .env file. Fill DATABASE_URL with connection string
- Download dependencies 
```sh
go mod tidy
```
- Either run directly on dev (with air) or compile into bin/main.exe
Dev (Hot reload)
```sh
air
```
or
```sh
go build -o ./bin/main.exe ./src
```
- Have Azure Core Tools installed
- Running locally:
```sh
func start
```

##

## Details
- Framework: [Echo](https://echo.labstack.com/)
- ORM: [GORM](https://gorm.io/)
