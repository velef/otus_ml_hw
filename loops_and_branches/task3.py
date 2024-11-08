"""
Написать упрощенную версию алгоритма RLE.
Алгоритм RLE объединяет подряд идущие символы в коэффициент и символ.

Пример:
    aaabbbbccccc -> 3a4b5c
    asssdddsssddd -> 1a3s3d3s3d
    abcba -> 1a1b1c1b1a
"""


def compress_using_rle(row: str) -> str:
    """Сжимает строку используя алгоритм RLE."""
    result = ''
    counter = 0

    if row:
        previous_char = row[0]

        for char in row:
            if char != previous_char:
                result += str(counter) + previous_char
                counter = 1

            else:
                counter += 1

            previous_char = char

        # В цикле значения добавляются только при смене символа,
        # поэтому последнюю последовательность надо добавть вручную
        result += str(counter) + previous_char

    return result


if __name__ == '__main__':
    print(value := input('Введите строку для сжатия: '), '->', compress_using_rle(value))
