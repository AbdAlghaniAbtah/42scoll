from abc import ABC, abstractmethod
from typing import Any, Protocol


class DataProcessor(ABC):
    
    def __init__(self):
        self.data = []
        self.counter = 0
        self.ingested_count = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass
    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if self.data:
            value = self.data.pop(0)
            self.counter += 1
            return (self.counter - 1, value)
        return (self.counter, "")



class NumericProcessor(DataProcessor):
    
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            if len(data) == 0:
                return False
            for item in data:
                if isinstance(item, (int, float)) == False:
                    return False
            return True
        return False
    
    def ingest(self, data: int | float | list[int | float]) -> None:
        if self.validate(data):
            if isinstance(data, (int, float)):
                self.data.append(str(data))
                self.ingested_count += 1
            elif isinstance(data, list):
                for item in data:
                    self.data.append(str(item))
                    self.ingested_count += 1    
            
        else:
            raise ValueError("Improper numeric data")



class TextProcessor(DataProcessor):
    
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list) and len(data) > 0:
            for item in data:
                if not isinstance(item, str):
                    return False
            return True
        return False

    def ingest(self, data: str | list[str]) -> None:
        if self.validate(data):
            if isinstance(data, str):
                self.data.append(data)   
                self.ingested_count += 1
            elif isinstance(data, list):
                for item in data:
                    self.data.append(item)
                    self.ingested_count += 1
        else:
            raise ValueError("Improper text data")


class LogProcessor(DataProcessor):


    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            for k, v in data.items():
                if not isinstance(k, str) or not isinstance(v, str):
                    return False
            return True
        if isinstance(data, list) and len(data) > 0:
            for item in data:
                if not isinstance(item, dict):
                    return False
                for k, v in item.items():
                    if not isinstance(k, str) or not isinstance(v, str):
                        return False
            return True
        return False

    def ingest(self, data: dict | list[dict]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
            
        items = [data] if isinstance(data, dict) else data
        for item in items:
            formatted_log = f"{item['log_level']}: {item['log_message']}"
            self.data.append(formatted_log)
            self.ingested_count += 1
class ExportPlugin(Protocol):
    
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass

class CreateJson(ExportPlugin):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        if not data:
            return
        items = []
        for i, item in enumerate(data):
            items.append(f'"item_{i+1}": "{item[1]}"')
        json_body = ", ".join(items)
        print(f"JSON Output: {{{json_body}}}")
        
class CreateCSV(ExportPlugin):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        val = [content for rank, content in data]
        print("CSV Output:")
        print(",".join(val))
    
class DataStream:
    def __init__(self):
        self.processors = []
    
    def register_processor(self, proc: DataProcessor) -> None:
        for p in self.processors:
            if p is proc:
                print(f"Processor {proc.__class__.__name__} is already registered, skipping.")
                return
        self.processors.append(proc)
    def process_stream(self, stream: list[Any]) -> None:
        for data in stream:
            f = False
            for proc in self.processors:
                if proc.validate(data):
                    try:
                        proc.ingest(data)
                        f = True
                        break
                    except ValueError as e:
                        continue
            if not f:
                print(f"DataStream error - Can't process element in stream: {data}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self.processors:
            print("No processor found, no data.")
            return
    
        for proc in self.processors:
            name = proc.__class__.__name__
            total = proc.ingested_count
            remaining = len(proc.data)
            print(f"{name}: total {total} items processed, remaining {remaining} on processor")
            
    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:

        for proc in self.processors:
            output_data = []
            for _ in range(nb):
                rank, content = proc.output()
                if content == "":
                    break
                output_data.append((rank, content))
            if output_data:
                plugin.process_output(output_data)


def main():
    print("=== Code Nexus - Data Pipeline ===")
    
    ds = DataStream()
    
    print("Initialize Data Stream...")
    ds.print_processors_stats() 

    print("\nRegistering Processors")
    ds.register_processor(NumericProcessor())
    ds.register_processor(TextProcessor())
    ds.register_processor(LogProcessor())

    first_batch = [
        'Hello world', 
        [3.14, -1, 2.71], 
        [{'log_level': 'WARNING', 'log_message': 'Telnet access! Use ssh instead'}, 
         {'log_level': 'INFO', 'log_message': 'User wil is connected'}], 
        42, 
        ['Hi', 'five']
    ]
    
    print(f"\nSend first batch of data on stream: {first_batch}")
    ds.process_stream(first_batch)
    ds.print_processors_stats()

    print("\nSend 3 processed data from each processor to a CSV plugin:")
    ds.output_pipeline(3, CreateCSV())
    ds.print_processors_stats()

    second_batch = [
        21, 
        ['I love AI', 'LLMs are wonderful', 'Stay healthy'], 
        [{'log_level': 'ERROR', 'log_message': '500 server crash'}, 
         {'log_level': 'NOTICE', 'log_message': 'Certificate expires in 10 days'}], 
        [32, 42, 64, 84, 128, 168], 
        'World hello'
    ]
    
    print(f"\nSend another batch of data: {second_batch}")
    ds.process_stream(second_batch)
    ds.print_processors_stats()

    print("\nSend 5 processed data from each processor to a JSON plugin:")
    ds.output_pipeline(5, CreateJson())
    ds.print_processors_stats()

if __name__ == "__main__":
    main()