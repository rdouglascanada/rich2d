from abc import ABC, abstractmethod


class Element(ABC):
    @abstractmethod
    def update(self):
        pass
