# Standard Libraries
from abc import ABC, abstractmethod


class Order(ABC):
    @abstractmethod
    def order_by(self) -> list[str]:
        ...


class DataInstance(ABC):
    @abstractmethod
    def __init__(self, model):
        self._model = model


class ListQuery(DataInstance):
    @abstractmethod
    def get_object_list(self):
        ...


class SingleQuery(DataInstance):
    @abstractmethod
    def get_object(self):
        ...


class BulkCreateInstance(DataInstance):
    @abstractmethod
    def bulk_create(self) -> list:
        ...


class CreateInstance(DataInstance):
    @abstractmethod
    def create(self):
        ...


class UpdateInstance(DataInstance):
    @abstractmethod
    def update(self):
        ...


class DeleteInstance(DataInstance):
    @abstractmethod
    def delete(self):
        ...


class PostRequestInstance(ABC):
    @abstractmethod
    def make_request(self):
        ...
