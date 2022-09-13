import sentry_sdk
from sentry_sdk.integrations.sqlalchemy import SqlalchemyIntegration

from app.config.settings import settings


class Sentry:

    def __init__(self):
        if settings.ENV == 'prod':
            sentry_sdk.init(
                dsn=settings.SENTRY_URL_INGEST_DATA,
                integrations=[SqlalchemyIntegration()],
                send_default_pii=True)
