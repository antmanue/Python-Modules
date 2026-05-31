import abc
import typing


class DataProcessor(abc.ABC):

    def __init__(self) -> None:
        self.struct_list: list[tuple[int, str]] = []
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
            raise ValueError("Improper numeric data")
        items = data if isinstance(data, list) else [data]
        for item in items:
            converted = str(item)
            self.struct_list.append((self.counter, converted))
            self.counter = self.counter + 1


class TextProcessor(DataProcessor):

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, str):
            return True
        elif data != ([]) and isinstance(data, list):
            for item in data:
                if not isinstance(item, str):
                    return False

            return True
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper string data")
        items = data if isinstance(data, list) else [data]
        for item in items:
            self.struct_list.append((self.counter, item))
            self.counter = self.counter + 1


class LogProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if (isinstance(data, dict)
                and "log_level" in data
                and "log_message" in data):
            return True
        elif (data != ([])
                and isinstance(data, list)):
            for item in data:
                if not (isinstance(item, dict)
                        or "log_level" not in item
                        or "log_message" not in item):
                    return False

            return True
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        items = data if isinstance(data, list) else [data]
        for item in items:
            converted = f"{item['log_level']}: {item['log_message']}"
            self.struct_list.append((self.counter, converted))
            self.counter = self.counter + 1


def main() -> None:
    print("=== Code Nexus - Data Processor ===")
    print()
    print("Testing Numeric Processor...")
    numeric_process = NumericProcessor()

    print(f"Trying to validate input '42': {numeric_process.validate(42)}")

    print(f"Trying to validate input"
          f" 'Hello': {numeric_process.validate('Hello')} ")

    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        numeric_process.ingest("foo")

    except ValueError as err:
        print(f"Got exception: {err}")

    print("Processing data: [1, 2, 3, 4, 5]")
    numeric_process.ingest([1, 2, 3, 4, 5])
    print("Extracting 3 values...")
    for i in range(3):
        num_id, num_val = numeric_process.output()
        print(f"Numeric value {num_id}: {num_val}")

    print()
    print("Testing Text Processor...")
    text_process = TextProcessor()

    print(f"Trying to validate input '42': {text_process.validate(42)}")

    print("Processing data: ['Hello', 'Nexus', 'World']")
    text_process.ingest(['Hello', 'Nexus', 'World'])
    print("Extracting 1 value...")
    tex_id, tex_val = text_process.output()
    print(f"Text value {tex_id}: {tex_val}")
    print()
    print("Testing Log Processor...")
    log_process = LogProcessor()
    print(f"Trying to validate input"
          f" 'Hello': {log_process.validate('Hello')} ")

    log_data = [
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}
    ]
    print(f"Processing data: {log_data}")
    log_process.ingest(log_data)

    print("Extracting 2 Values...")
    for i in range(2):
        log_id, log_val = log_process.output()
        print(f"Log entry {log_id}: {log_val}")


if __name__ == "__main__":
    main()
