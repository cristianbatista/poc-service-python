from loguru import logger

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.config.settings import settings
from app.interface.consumers.create_person.consumer import (consumer_cancel_task_stop_consumer,
                                                            create_consumer_task, initialize_consumer)
from app.interface.api.v1.endpoints.health import router as health_router
from app.interface.api.v1.endpoints.person import router as person_router


def create_app():
    app = FastAPI(title=settings.PROJECT_NAME)

    @app.on_event("startup")
    async def startup_event():
        logger.info("Initializing API ...")
        await initialize_consumer()
        await create_consumer_task()

    @app.on_event("shutdown")
    async def shutdown_event():
        logger.info("Shutting down API")
        await consumer_cancel_task_stop_consumer()

    # Middlewares
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_HOSTS,
        allow_credentials=True,
        allow_methods=settings.ALLOWED_METHODS,
        allow_headers=settings.ALLOWED_HEADERS,
    )

    # define routers
    app.include_router(health_router, tags=['health'], prefix="/health")
    app.include_router(person_router, tags=['person'], prefix="/person")

    return app


app = create_app()
