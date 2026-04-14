import json

json_str = '{"name": "Alice", "age": 30, "city": "New York"}'

py_obj = json.loads(json_str)

print(py_obj)