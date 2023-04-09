# Standard Libraries
from abc import ABC, abstractmethod


class IConcreteFactory(ABC):
    
    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def update(self):
        pass    
