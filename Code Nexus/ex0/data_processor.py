from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    
    def __init__(self):
        self.data = []
        self.counter = 0
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
            elif isinstance(data, list):
                for item in data:
                    self.data.append(str(item))    
            
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
            elif isinstance(data, list):
                for item in data:
                    self.data.append(item)
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

    

def test_numeric_processor():
    print("\nTesting Numeric Processor...")
    processor = NumericProcessor()
    lis = [42, "Hello"]
    for item in lis:
        print(f"Trying to validate input {item}:", processor.validate(item))
    print("Test invalid ingestion of string 'foo'  without prior validation: ")
    try:
        processor.ingest("foo")
    except ValueError as e:
        print(f"Got exception: {e}")
    list_int = [1, 2, 3, 4, 5]
    print(f"Processing data: {list_int}")
    processor.ingest(list_int)
    print("Extracting 3 values...")
    for i in range(3):
        _, value = processor.output()
        print(f"Numeric value {i}: {value}")
        

def test_text_processor():
    print("\nTesting Text Processor...")
    processor = TextProcessor()
    print(f"Trying to validate input '42': {processor.validate(42)}")
    data_to_process = ["Hello", "Nexus", "World"]
    print(f"Processing data: {data_to_process}")
    try:
        processor.ingest(data_to_process)
    except ValueError as e:
        print(f"Got exception: {e}")
        
    print("Extracting 1 value...")
    _, value = processor.output()
    print(f"Text value 0: {value}")

def test_log_processor():
    print("\nTesting Log Processor...")
    processor = LogProcessor()

    print(f"Trying to validate input 'Hello': {processor.validate('Hello')}")
    log_data = [
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}
    ]
    print(f"Processing data: {log_data}")
    try:
        processor.ingest(log_data)
    except ValueError as e:
        print(f"Got exception: {e}")
    
    print(f"Extracting 2 values...")
    for i in range(2):
        _, value = processor.output()
        print(f"Log entry {i}: {value}")

def main():
    print("=== Code Nexus - Data Processor ===")
    test_numeric_processor()
    test_text_processor()
    test_log_processor()

if __name__ == "__main__":
    main()