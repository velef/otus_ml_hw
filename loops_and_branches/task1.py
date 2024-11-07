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
    print('Введите целое положительное число')
    print(input_value := input(), '->', compress_to_single(input_value))
