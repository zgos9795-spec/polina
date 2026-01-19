"""
Конвертер CSV в JSON
Преобразует данные из CSV формата в JSON
"""

import csv
import json


def read_csv_file(input_file, separator=','):
    """
    Читает данные из CSV файла

    Args:
        input_file (str): Путь к CSV файлу
        separator (str): Разделитель полей (',' или ';')

    Returns:
        list: Список словарей с данными
    """
    with open(input_file, 'r', encoding='utf-8') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=separator)
        return list(csvreader)


def write_json_file(info, output_file, spaces=2):
    """
    Сохраняет данные в JSON файл

    Args:
        info (list): Данные для сохранения
        output_file (str): Путь к JSON файлу
        spaces (int): Отступ для форматирования
    """
    with open(output_file, 'w', encoding='utf-8') as jsonfile:
        json.dump(info, jsonfile, ensure_ascii=False, indent=spaces)


def get_delimiter(filename):
    """
    Определяет разделитель в CSV файле

    Args:
        filename (str): Путь к CSV файлу

    Returns:
        str: Разделитель (',' или ';')
    """
    with open(filename, 'r', encoding='utf-8') as f:
        sample = f.readline()

    return ';' if ';' in sample else ','


def csv_to_json_converter(source_csv, target_json=None, sep=None):
    """
    Основная функция конвертации

    Args:
        source_csv (str): Путь к CSV файлу
        target_json (str): Путь к JSON файлу (опционально)
        sep (str): Разделитель CSV (опционально)

    Returns:
        bool: True при успешной конвертации
    """
    try:
        # Определяем выходной файл
        if not target_json:
            if source_csv.endswith('.csv'):
                target_json = source_csv[:-4] + '.json'
            else:
                target_json = source_csv + '.json'

        # Определяем разделитель
        if not sep:
            sep = get_delimiter(source_csv)

        # Читаем CSV
        records = read_csv_file(source_csv, sep)

        # Сохраняем JSON
        write_json_file(records, target_json)

        # Выводим результат
        print(f"✓ Конвертация завершена")
        print(f"  CSV: {source_csv}")
        print(f"  JSON: {target_json}")
        print(f"  Записей: {len(records)}")

        return True

    except FileNotFoundError:
        print(f"✗ Ошибка: файл '{source_csv}' не найден")
        return False
    except Exception as err:
        print(f"✗ Ошибка: {err}")
        return False


def start_program():
    """
    Точка входа в программу
    """
    print("=== Конвертер CSV в JSON ===")

    # Запрашиваем имя CSV файла
    csv_path = input("Введите имя CSV файла: ").strip()

    if not csv_path:
        print("✗ Не указано имя файла")
        return

    # Запускаем конвертацию
    csv_to_json_converter(csv_path)


# Запуск программы
if __name__ == "__main__":
    start_program()