import json

# Укажите имя файла
input_json = "input.json"  # ← если файл называется по-другому, поменяйте тут

# Открываем и читаем JSON
with open(input_json, 'r') as json_file:
    json_data = json.load(json_file)

# Считаем сумму score * weight
total_sum = 0
for entry in json_data:
    total_sum += entry['score'] * entry['weight']

# Выводим результат
print(f"Сумма score * weight = {total_sum}")