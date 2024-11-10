"""
Написать функцию, которая будет перводит snake_case в CamelCase и наоборот.

Функция сама определяет, какой формат ей передали.
Можно добавить ключевой аргумент, который будет принудительно возвращать один из форматов.

Пример:

    otus_course -> OtusCourse
    PythonIsTheBest -> python_is_the_best
"""


def is_snake_case(row: str) -> bool:
    """Вернёт True, если в строке есть нижнее подчёркивание."""
    return bool(row.count('_'))


def is_camel_case(row: str) -> bool:
    """Вернёт True, если в строке есть хоть одна заглавная буква."""
    return any(char.isupper() for char in row)


def to_snake_case(row: str) -> str:
    """Конвертирует строку в формат snake_case."""
    result = ''

    for i, char in enumerate(row):
        if char.isupper():
            result += char.lower() if i == 0 else '_' + char.lower()

        else:
            result += char

    return result


def to_camel_case(row: str) -> str:
    """Конвертирует строку в формат CamelCase."""
    return ''.join(word.capitalize() for word in row.split('_'))


def convert(row: str) -> str:
    """Перводит snake_case в CamelCase и наоборот

    :param row: Строка, которую надо отконвертировать.
    :param to_snake: Если True, строка отконвертируется в snake_case, иначе в CamelCase.
    """
    if is_snake_case(row):
        return to_camel_case(row)

    return to_snake_case(row)
