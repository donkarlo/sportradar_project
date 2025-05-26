from abc import ABC, abstractmethod


class TaskBase(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def run(self):
        pass