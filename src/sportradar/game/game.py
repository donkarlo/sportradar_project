from abc import ABC, abstractmethod

class Game(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def get_score(self)->int:
        pass