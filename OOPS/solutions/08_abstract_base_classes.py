from abc import ABC, abstractmethod
from typing import Any, List, Dict
import json, io, csv

class Serializer(ABC):
    @abstractmethod
    def dumps(self, obj) -> str: ...
    @abstractmethod
    def loads(self, s: str): ...

class JsonSerializer(Serializer):
    def dumps(self, obj) -> str:
        return json.dumps(obj, ensure_ascii=False)
    def loads(self, s: str):
        return json.loads(s)

class CsvSerializer(Serializer):
    """Serialize list[dict[str, Any]] to CSV and back."""
    def dumps(self, rows: List[Dict[str, Any]]) -> str:
        if not rows:
            return ""
        output = io.StringIO()
        fieldnames = list(rows[0].keys())
        writer = csv.DictWriter(output, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
        return output.getvalue()

    def loads(self, s: str):
        if not s.strip():
            return []
        input_io = io.StringIO(s)
        reader = csv.DictReader(input_io)
        return [dict(row) for row in reader]

def main():
    j = JsonSerializer()
    data = {"name": "Alice", "age": 30}
    s = j.dumps(data); print(s); print(j.loads(s))

    rows = [{"id": 1, "name": "A"}, {"id": 2, "name": "B"}]
    c = CsvSerializer()
    csv_text = c.dumps(rows); print(csv_text); print(c.loads(csv_text))

if __name__ == "__main__":
    main()
