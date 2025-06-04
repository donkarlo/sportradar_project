class Card:
    def __init__(self, value:Union[int, str], type:str):
        self._value = value
        self._type = type