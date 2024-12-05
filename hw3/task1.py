"""
Написать функцию, которая будет переводит snake_case в CamelCase и наоборот.

Функция сама определяет, какой формат ей передали.
Можно добавить ключевой аргумент, который будет принудительно возвращать один из форматов.

Пример:

    otus_course -> OtusCourse
    PythonIsTheBest -> python_is_the_best
"""

import re


def is_snake_case(row: str) -> bool:
    """Вернёт True, если в строке есть нижнее подчёркивание."""
    return bool(row.count('_'))


def is_camel_case(row: str) -> bool:
    """Вернёт True, если в строке есть хоть одна заглавная буква."""
    return any(char.isupper() for char in row)


def to_snake_case(row: str) -> str:
    """Конвертирует строку в формат snake_case из CamelCase."""
    return '_'.join(char.lower() for char in re.findall(r'[A-Z][^A-Z]*', row))


def to_camel_case(row: str) -> str:
    """Конвертирует строку в формат CamelCase из snake_case."""
    return ''.join(word.capitalize() for word in row.split('_'))


def convert(row: str) -> str:
    """Переводит snake_case в CamelCase и наоборот."""
    if is_snake_case(row):
        return to_camel_case(row)

    return to_snake_case(row)
