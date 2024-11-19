"""
Пользователь вводит целое число.
Программа складывает все цифры числа, с полученным числом - то же самое,
и так до тех пор, пока не получится однозначное число.

Пример:
    545 -> 5
    12345 -> 6
"""


def compress_to_single(row: str) -> int:
    """Поэлементное сложение чисел в строке до получения однозначного числа."""

    while True:
        total = sum(map(int, row))

        if total // 10 == 0:
            break

        row = str(total)

    return total


if __name__ == '__main__':
    msg = 'Введите целое положительное число: '
    input_value = input(msg)

    while not input_value.isdigit():
        input_value = input(msg)

    print(input_value, '->', compress_to_single(input_value))
