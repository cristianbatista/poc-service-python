from loguru import logger
from sqlalchemy.exc import SQLAlchemyError

from app.infrastructure.database.postgre import SessionLocal, engine
from app.config import settings
from app.infrastructure.models import Base


def create_db_schema_and_tables():
    """Create all tables if they do not exist.
    Raises:
        - `SQLAlchemyError`
    """
    try:
        Base.metadata.create_all(bind=engine, checkfirst=True)
    except SQLAlchemyError as e:
        logger.error(f'[-] Error encountered while connected to {settings.POC_SERVICE_DB_URL}: {e}')
        raise SQLAlchemyError


def get_db():
    """Instantiates and yields a database session.
    Returns:
        - SessionLocal
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
