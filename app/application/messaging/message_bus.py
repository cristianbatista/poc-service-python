from abc import ABC, abstractmethod


class MessageBus(ABC):
    @staticmethod
    @abstractmethod
    async def send_message(topic: str, message: dict):
        raise NotImplementedError()
