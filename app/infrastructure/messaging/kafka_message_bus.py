import json

from app.config.settings import settings
from aiokafka import AIOKafkaProducer
from loguru import logger


class KafkaMessageBus:

    @staticmethod
    async def send_message(topic: str, message: dict):
        logger.info("Start send message")
        producer = AIOKafkaProducer(bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS)
        # get cluster layout and initial topic/partition leadership information
        await producer.start()

        try:
            # produce message
            logger.info(f"Send and wait message - {message}")
            await producer.send_and_wait(topic, json.dumps(message).encode('utf-8'))
        except Exception as e:
            logger.error(f"Error - Send and wait message - {str(e)}")
            raise e
        finally:
            # wait for all pending messages to be delivered or expire.
            await producer.stop()
            logger.info("Stop producer")