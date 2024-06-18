# Azure Function Stack benchmark

This repository consists of the same Azure Function Implementation for the following languages in order to benchmark them:
- Go
- TypeScript
- Java
- Python

The benchmarks include a CRUD application that is designed to connect into a postgres database


## Folder Structure

- Each language contains it's own folder
- The compose.yaml file is a (Docker/Podman) Compose file that sets a local database
- The db folder contains the migration file that sets the database structure

## Local Result

Testing using local database, from a cold start making a GET request into content endpoint.

Language | Time (ms)
---|---
Go | 266
TypeScript | 344
Python | 2350
Java | 5200
