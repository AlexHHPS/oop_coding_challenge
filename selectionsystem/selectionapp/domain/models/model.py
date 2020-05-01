from abc import ABC, abstractmethod


class Model(ABC):
    @abstractmethod
    def hydrate(self, data):
        pass
