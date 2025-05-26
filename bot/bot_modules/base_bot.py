from abc import ABC, abstractmethod


class BaseBot(ABC):
    """
    Абстрактный класс для наследования.
    Заставляет использовать метод run() иначе - ошибка.
    """

    def __init__(self, config):
        self.config = config

    @abstractmethod
    def run(self):
        pass
