# Java + Spring Cloud

- Works for Java 17 and 21

This project implements 2 endpoints:
1. /api/AzureWebAdapter/hello returns hello world
1. /api/content CRUD implementation
    1. POST /api/AzureWebAdapter/content CREATE resource Body: {"color": "#ffffff", "title": "white"}
    1. GET /api/AzureWebAdapter/content?id=1 READ resource
    1. PUT /api/AzureWebAdapter/content?id=1 UPDATE resource Body: {"color": "#ffffff", "title": "white"}
    1. DELETE /api/AzureWebAdapter/content?id=1 DELETE resource

## Install

- Java and Maven Installed
- Have a running Postgres database all setup
- Under application.properties, set the proper connection details
- Have Azure Core Tools installed
- Compile
```sh
mvn package
```
- Running locally:
```sh
mvn azure-functions:run
```

##

## Details
- Spring Boot 3
- ORM: Spring Data JPA
