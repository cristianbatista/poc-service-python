import asyncio
import logging

import aiokafka

from app.config.settings import settings
# global variables
from app.interface.consumers.create_person.create_person_worker import (
    CreatePersonWorker,
)

# TODO: verificar o loguru pois omitiu os logs do kafka
# from loguru import logger


consumer_task = None
consumer_created_person_event = None

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


async def initialize_consumer():
    loop = asyncio.get_event_loop()
    global consumer_created_person_event
    logger.info(
        f"Initializing KafkaConsumer for topic {settings.KAFKA_TOPIC}, group_id {settings.KAFKA_CONSUMER_GROUP} and using bootstrap servers {settings.KAFKA_BOOTSTRAP_SERVERS}"
    )

    consumer_created_person_event = aiokafka.AIOKafkaConsumer(
        settings.KAFKA_TOPIC,
        loop=loop,
        bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
        group_id=settings.KAFKA_CONSUMER_GROUP,
    )
    # get cluster layout and join group
    await consumer_created_person_event.start()


async def receive_message(consumer: aiokafka.AIOKafkaConsumer):
    try:
        # consume messages
        async for msg in consumer:
            await CreatePersonWorker().execute(msg)
    finally:
        # will leave consumer group; perform autocommit if enabled
        logger.warning("Stopping consumer")
        await consumer.stop()


async def create_consumer_task():
    global consumer_task
    consumer_task = asyncio.create_task(receive_message(consumer_created_person_event))
    return consumer_task


async def consumer_cancel_task_stop_consumer():
    consumer_task.cancel()
    await consumer_created_person_event.stop()
