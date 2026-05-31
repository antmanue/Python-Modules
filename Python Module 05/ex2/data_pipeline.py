import abc
import typing


class ExportPlugin(typing.Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


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
        elif data != ([]) and isinstance(data, list):
            for item in data:
                if not (isinstance(item, dict) or "log_level"
                        not in item or "log_message"
                        not in item):
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


class DataStream():

    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for element in stream:
            processed = False

            for proc in self.processors:
                if proc.validate(element):
                    proc.ingest(element)
                    processed = True
                    break

            if not processed:
                print(f"DataStream error - Can't process element in "
                      f"stream: {element}")

    def print_processors_stats(self) -> None:
        if not self.processors:
            print("No processor found, no data")
            return
        for proc in self.processors:
            remain = len(proc.struct_list)
            space_class = proc.__class__.__name__
            space_class = space_class.replace("Processor", " Processor")
            print(f"{space_class}: total {proc.counter} items "
                  f"processed, remaining {remain} on processor")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self.processors:
            extracted_batch: list[tuple[int, str]] = []
            for _ in range(nb):
                if proc.struct_list:
                    extracted_batch.append(proc.output())

            plugin.process_output(extracted_batch)


class JSONExporter:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        if not data:
            return
        json_items = [
            f'"item_{id_num}": "{message}"' for id_num, message in data]
        final_json = "{" + ", ".join(json_items) + "}"
        print("JSON Output:")
        print(final_json)


class CSVExporter:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        if not data:
            return

        csv_row = ", ".join(message for _, message in data)
        print("CSV Output:")
        print(csv_row)


def main() -> None:
    first_batch = [
                'Hello world',
                [3.14, -1, 2.71],
                [
                    {'log_level': 'WARNING',
                     'log_message': 'Telnet access! Use ssh instead'},
                    {'log_level': 'INFO',
                     'log_message': 'User wil is connected'}
                ],
                42,
                ['hi', 'five']
    ]
    second_batch = [
        21,
        ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
        [
            {'log_level': 'ERROR',
             'log_message': '500 server crash'},
            {'log_level': 'NOTICE',
             'log_message': 'Certificate expires in 10 days'}
        ],
        [32, 42, 64, 84, 128, 168],
        'World hello'
    ]

    print("=== Code Nexus - Data Pipeline ===")
    print("\nInitialize Data Stream...")
    print("== DataStream statistics ==")
    data_flow = DataStream()
    data_flow.print_processors_stats()

    print("\nRegistering Numeric Processor")
    proc_numeric = NumericProcessor()
    proc_text = TextProcessor()
    proc_log = LogProcessor()

    data_flow.register_processor(proc_numeric)
    data_flow.register_processor(proc_text)
    data_flow.register_processor(proc_log)

    print("\nSend first batch of data on stream:", first_batch)
    data_flow.process_stream(first_batch)

    print("== DataStream statistics ==")
    data_flow.print_processors_stats()

    print("\nSend 3 processed data from each processor to a CSV plugin:")
    csv_exporter = CSVExporter()
    data_flow.output_pipeline(3, csv_exporter)

    print("== DataStream statistics ==")
    data_flow.print_processors_stats()

    print("\nSend another batch of data:", second_batch)
    data_flow.process_stream(second_batch)

    print("== DataStream statistics ==")
    data_flow.print_processors_stats()

    print("\nSend 5 processed data from each processor to a JSON plugin:")
    json_exporter = JSONExporter()
    data_flow.output_pipeline(5, json_exporter)

    print("== DataStream statistics ==")
    data_flow.print_processors_stats()


if __name__ == "__main__":
    main()
