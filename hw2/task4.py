"""
Шифр Цезаря.

Пользователь вводит строку и ключ шифра.
Программа должна вывести зашифрованную строку (со сдвигом по ключу).
Сдвиг циклический, используем только латинский алфавит, пробелы не шифруются.

Пример:
    Dog, 2 -> Fqi
    Zak zak, 3 -> Cdn cdn
    Python is the BEST, 5 -> Udymts nx ymj GJXY
"""

LOWER_MIN_UNICODE = ord('a')
LOWER_MAX_UNICODE = ord('z')

UPPER_MIN_UNICODE = ord('A')
UPPER_MAX_UNICODE = ord('Z')

ALPHABET_LENGTH = 25


def encrypt_using_caesar(input_sequence: str, key: int) -> str:
    """Прогоняет строку через цифр Цезаря с заданным ключом."""
    encoded = ''
    key = key if key <= ALPHABET_LENGTH else key % ALPHABET_LENGTH

    for char in input_sequence:
        char_unicode = ord(char)
        shifted_unicode = char_unicode + key

        if UPPER_MIN_UNICODE <= char_unicode <= UPPER_MAX_UNICODE:
            if shifted_unicode > UPPER_MAX_UNICODE:
                shifted_unicode = shifted_unicode - UPPER_MAX_UNICODE + UPPER_MIN_UNICODE - 1

        elif LOWER_MIN_UNICODE <= char_unicode <= LOWER_MAX_UNICODE:
            if shifted_unicode > LOWER_MAX_UNICODE:
                shifted_unicode = shifted_unicode - LOWER_MAX_UNICODE + LOWER_MIN_UNICODE - 1

        else:
            shifted_unicode = char_unicode

        encoded += chr(shifted_unicode)

    return encoded


if __name__ == '__main__':
    input_value = input('Введите строку, которую для шифрования, используйте английские буквы: ')

    msg = 'Введите ключ (целое число): '
    encoding_key = input(msg)
    while not encoding_key.isdigit():
        encoding_key = input(msg)

    print(input_value, encoding_key, '->', encrypt_using_caesar(input_value, int(encoding_key)))
