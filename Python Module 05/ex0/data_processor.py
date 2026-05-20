import abc
import typing

class DataProcessor(abc.ABC):
    
    def __init__(self) -> None:
        self.struct_list = []
        self.counter = 0

    @abc.abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abc.abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        removed = self.struct_list.pop(0)
        
        return removed
    
class NumericProcessor(DataProcessor):

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        elif data != ([]) and isinstance(data, list):
            for item in data:
                if not isinstance(item, (int, float)):
                    return False

            return True
        return False

    def ingest(self, data: typing.Any) -> None:
        if not self.validate(data):
            raise ValueError ("Improper numeric data")
        items = data if isinstance(data, list) else [data]
        for item in items:
            converted = data.pop(0)
            struct_list = 

