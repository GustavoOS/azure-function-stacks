# TypeScript language

This project implements 2 endpoints:
1. /api/hello returns hello world
1. /api/content CRUD implementation
    1. POST /api/content CREATE resource Body: {"color": "#ffffff", "title": "white"}
    1. GET /api/content?id=1 READ resource
    1. PUT /api/content?id=1 UPDATE resource Body: {"color": "#ffffff", "title": "white"}
    1. DELETE /api/content?id=1 DELETE resource

## Install

- Have node 20 and pnpm installed [pnpm installation](https://pnpm.io/pt/installation)
- Have a running Postgres database all setup
- Create a .env file. Fill DATABASE_URL with connection string
- Download dependencies 
```sh
pnpm install
```
- Compile
```sh
pnpm build
```
- Have Azure Core Tools installed
- Running locally:
```sh
func start --verbose
```

##

## Details
- ORM: [Drizzle](https://orm.drizzle.team/)
