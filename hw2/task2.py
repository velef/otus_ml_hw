"""
Кинотеатр.

Дан список списков, каждый вложенный список состоит из 1 и 0.
Количество вложенных списков - количество рядов.

Пользователь вводит сколько билетов ему требуется.

Программа должна найти ряд, где можно приобрести нужно количество билетов (места должны быть рядом).
Если таких рядов несколько, то ближайший к экрану (ближайшим считается нулевой ряд).
Еcли таких мест нет, то вывести False

Пример:
    [[0, 1, 1, 0], [1, 0, 0, 0], [0, 1, 0, 0]], 2 -> 1
    [[0, 1, 1, 0], [1, 0, 1, 0], [1, 1, 0, 1]], 2 -> False
"""


def check_seats(rows: list[list[int]], tickets_amount: int) -> bool or int:
    """Ищет список где последовательность идущих подряд нулей соотвествтует заданному значению."""
    suited_row_index = None

    for i, row in enumerate(rows):
        if len(row) < tickets_amount:
            continue

        free_seats_chain = 0

        for j, seat in enumerate(row):
            free_seats_chain = free_seats_chain + 1 if seat == 0 else 0

            if free_seats_chain == tickets_amount:
                suited_row_index = i
                break

        if suited_row_index is not None:
            break

    return suited_row_index if suited_row_index is not None else False


if __name__ == '__main__':
    msg = 'Сколько билетов Вам трубуется? '

    while (required_tickets_amount := input(msg)) == '0' or not required_tickets_amount.isdigit():
        print('Укажите целое положительное число, отличное от 0')

    required_tickets_amount = int(required_tickets_amount)
    rows_configuration = [[0, 1, 1, 0], [1, 0, 1, 0], [0, 1, 0, 0]]
    result = check_seats(rows_configuration, required_tickets_amount)

    if result is False:
        print(f'Нет ряда с количеством свободных мест {required_tickets_amount}')

    else:
        print(f'Ваш ряд №{result}')

