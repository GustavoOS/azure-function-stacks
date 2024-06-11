# Azure Function Stack benchmark

This repository consists of the same Azure Function Implementation for the following languages in order to benchmark them:
- Go
- JavaScript
- Java
- Python

The benchmarks include a CRUD application that is designed to connect into a postgres database


## Folder Structure

- Each language contains it's own folder
- The compose.yaml file is a (Docker/Podman) Compose file that sets a local database
- The db folder contains the migration file that sets the database structure
