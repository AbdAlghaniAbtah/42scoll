from abc import ABC, abstractmethod
from typing import Any


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
            print("No processor found, no data to process.")
            return
    
        for proc in self.processors:
            name = proc.__class__.__name__
            total = proc.ingested_count
            remaining = len(proc.data)
            print(f"{name}: total {total} items processed, remaining {remaining} on processor")
            
def main():
    print("=== Code Nexus - Data Stream ===\n")
    print("Initialize Data Stream...")
    ds = DataStream()
    ds.print_processors_stats() 

    print("\nRegistering Numeric Processor\n")
    num_proc = NumericProcessor()
    ds.register_processor(num_proc)

    batch = [
        'Hello world', 
        [3.14, -1, 2.71], 
        [
            {'log_level': 'WARNING', 'log_message': 'Telnet access! Use ssh instead'}, 
            {'log_level': 'INFO', 'log_message': 'User wil is connected'}
        ], 
        42, 
        ['Hi', 'five']
    ]

    print(f"Send first batch of data on stream: {batch}")
    ds.process_stream(batch)
    ds.print_processors_stats()

    print("\nRegistering other data processors")
    text_proc = TextProcessor()
    log_proc = LogProcessor()
    ds.register_processor(text_proc)
    ds.register_processor(log_proc)

    print("\nSend the same batch again")
    ds.process_stream(batch) 
    ds.print_processors_stats()

    print("\nConsume some elements from the data processors: Numeric 3, Text 2, Log 1")
    for _ in range(3): num_proc.output()
    for _ in range(2): text_proc.output()
    for _ in range(1): log_proc.output()

    ds.print_processors_stats()

if __name__ == "__main__":
    main()