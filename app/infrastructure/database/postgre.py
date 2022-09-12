from ddtrace import Pin, patch
from loguru import logger
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.schema import CreateSchema
from app.config.settings import settings
from sqlalchemy import create_engine

# patch before importing `create_engine`
patch(sqlalchemy=True)

# Creates the database schema
try:
    engine = create_engine(settings.POSTGRE_DATABASE_URL, pool_pre_ping=True)

    # TODO: verficar se faz sentido criar o schema (?)
    # if not engine.dialect.has_schema(engine, settings.POC_SERVICE_DB_SCHEMA):
    #    engine.execute(CreateSchema(settings.POC_SERVICE_DB_SCHEMA))

    # Use a PIN to specify metadata related to this engine
    Pin.override(engine, service=settings.PROJECT_NAME)
except SQLAlchemyError as e:
    logger.error(f'[-] Error encountered while connected to {settings.POC_SERVICE_DB_URL}: {e}')
    raise e


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
