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
            converted = str(item)
            self.struct_list.append((self.counter, converted))
            self.counter = self.counter + 1

class StringProcessor(DataProcessor):

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, str):
            return True
        elif data != ([]) and isinstance(data, list):
            for item in data:
                if not isinstance(item, str):
                    return False

            return True
        return False

    def ingest(self, data: typing.Any) -> None:
        if not self.validate(data):
            raise ValueError ("Improper string data")
        items =  data if isinstance(data, list) else [data]
        for item in items:
            self.struct_list.append((self.counter, item))
            self.counter = self.counter + 1

def main() -> None:
    print("Testing Numeric Processor...")
    numeric_process = NumericProcessor()

    print(f"Trying to validate input '42': {numeric_process.validate(42)}")

    print(f"Trying to validate input 'Hello': {numeric_process.validate('Hello')} ")

if __name__ == "__main__":
    main()