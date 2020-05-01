from abc import ABC, abstractmethod


class Command(ABC):

    @abstractmethod
    def execute(self):
        """The required execute method which all command obejcts will use"""