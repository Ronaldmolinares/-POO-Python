from abc import ABC, abstractmethod


class BaseUser(ABC):
    @abstractmethod
    def request_book(self, title: str):
        pass
