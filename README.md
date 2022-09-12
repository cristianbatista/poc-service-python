# FastAPI com Kafka Consumer

Este projeto mostra como usar um **Kafka Consumer** e uma _interface_ API Web Python usando
**FastAPI**. 

## Stack

- `python>=3.9` usando `fastapi` como framework web.
- `aiokafka` biblioteca para interagir com **Kafka**.
- `alembic` ferramenta para mudanças no banco de dados (_migration_ e _seed_).

## Pré requisitos para ambiente de desenvolvimento
- [python 3.9+](https://www.python.org/downloads/release/python-3914/) 
- [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html)
- [docker-compose](https://docs.docker.com/compose/install/)

## Setup

```bash
$ make install
```

Preparando o banco de dados, executando os _migrations_ e _seeds_:
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

Tests:
```bash
$ make tests
``` 