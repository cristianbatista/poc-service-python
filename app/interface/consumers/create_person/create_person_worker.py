from loguru import logger


class CreatePersonWorker:

    async def execute(self, message: dict):
        logger.info(f"Create Person Worker received message - {message}")
