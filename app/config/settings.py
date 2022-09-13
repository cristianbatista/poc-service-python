from typing import List

from pydantic import BaseSettings


class Settings(BaseSettings):

    # Environment
    ENV: str = "development"

    # Project
    PROJECT_NAME: str = "poc-service-python"

    # API
    PORT: int = 8000

    # Security
    ALLOWED_HOSTS: List[str] = ["*"]
    ALLOWED_METHODS: List[str] = ["*"]
    ALLOWED_HEADERS: List[str] = ["*"]

    # Kafka
    KAFKA_TOPIC: str = "my_topic"
    KAFKA_CONSUMER_GROUP: str = "group-test"
    KAFKA_BOOTSTRAP_SERVERS: str = "localhost:19092"

    # Database
    POSTGRE_DATABASE_USER: str = "poc"
    POSTGRE_DATABASE_PASSWORD: str = "poc"
    POSTGRE_DATABASE_NAME: str = "poc"
    POSTGRE_DATABASE_HOST: str = "127.0.0.1"
    POSTGRE_DATABASE_PORT: int = 5432
    POSTGRE_DATABASE_SCHEMA: str = "public"
    POSTGRE_DATABASE_POOL_SIZE: int = 5
    POSTGRE_DATABASE_URL: str = f"postgresql://{POSTGRE_DATABASE_USER}:{POSTGRE_DATABASE_PASSWORD}@{POSTGRE_DATABASE_HOST}:{POSTGRE_DATABASE_PORT}/{POSTGRE_DATABASE_NAME}"

    # Sentry
    SENTRY_URL_INGEST_DATA: str = "https://05e1960517334d9d899e556a1859a8bd@o302946.ingest.sentry.io/6663472"

settings = Settings()
