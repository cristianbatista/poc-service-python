# FastAPI com Kafka Consumer

Arquétipo Python -  WebAPI utilizando o framework _FastAPI_ e _aoiokafka_ para publicar e consumir mensagens (Pub/Sub) 

## Stack

- `python>=3.9` 
- `fastapi` framework web.
- `aiokafka` biblioteca para interagir com **Kafka** (async).
- `alembic` ferramenta para gerenciar estruturas de banco de dados (_migration_ e _seed_).

## Pré requisitos para ambiente de desenvolvimento
- [python 3.9+](https://www.python.org/downloads/release/python-3914/) 
- [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html)
- [docker-compose](https://docs.docker.com/compose/install/)

## Setup

```bash
$ make install
```
Database | gerar _migrations_:
```bash
$ alembic revision --autogenerate -m "create table person"
```

Database | executar _migrations_:
```bash
$ alembic upgrade head
```

Iniciando a API e o _Consumer_:

```bash
$ make run-api
``` 

API Docs:
```
http://localhost:8000/docs
```

Lint
```bash
$ make lint
```

Format
```bash
$ make format
```

Tests:
```bash
$ make tests
``` 

### TO DO
- [ ] tests all layers
- [ ] integration test
- [ ] make coverage
- [ ] containers dockers
- [ ] pagination GET API
- [ ] handle erros API
- [ ] auth key cloack
- [ ] CI/CD (migration)