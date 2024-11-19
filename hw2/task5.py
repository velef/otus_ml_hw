"""
Табель успеваемости.

Пользователь в бесконечном цикле (пока не будет введена пустая строка) вводит строки вида:
    'название предмета' 'фамилия ученика' 'оценка'

После окончания ввода программа выводит в консоль `Название предмета`,
далее список учеников и все их оценки в виде таблицы.

Пример:

    Математика Иванов 5
    Математика Иванов 4
    Литература Иванов 3
    Математика Петров 5
    Литература Сидоров 3
    Литература Петров 5
    Литература Иванов 4
    Математика Сидоров 3
    Математика Петров 5

    Математика
        Иванов 5 4
        Петров 5 5
        Сидоров 3

    Литература
        Ивванов 3 4
        Сидоров 3
        Петров 5
"""


Card = dict[str, dict[str, list[str]]]
Note = list[str]


def add_note(note: Note, card: Card) -> None:
    """Добавляет информацию в выбранный табель успеваемости."""
    discipline, student_name, points = note
    card.setdefault(discipline, {})
    card[discipline].setdefault(student_name, []).append(points)


def show_card(card: Card) -> None:
    """Выводит табель успеваемости на экран."""
    for discipline, student_info in card.items():
        print(discipline)

        for student_name, student_points in student_info.items():
            print(f'\t{student_name}:', ' '.join(student_points))


if __name__ == '__main__':
    print('Вас приветствует электронный табель успеваемости!')
    report_card = {}

    msg = 'Введите через пробел название предмета, фамилию ученика и его оценку: '
    while (note := input(msg)) != '':
        note = note.split(' ')

        if len(note) != 3:
            print('Данные введены некорректно')

        else:
            add_note(note, report_card)

    show_card(report_card)
