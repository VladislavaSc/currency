import json

# Преобразование объекта Python в строку JSON
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
json_string = json.dumps(my_dict)
print(json_string)

# Преобразование строки JSON в объект Python
json_string = '{"name": "John", "age": 30, "city": "New York"}'
my_dict = json.loads(json_string)
print(my_dict)

# Чтение данных из файла и преобразование в объект Python
with open('data.json', 'r') as f:
    data = json.load(f)
print(data)

# Запись данных в файл в формате JSON
with open('data.json', 'w') as f:
    json.dump(data, f)

    