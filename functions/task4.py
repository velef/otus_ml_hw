"""
Пользователь в бесконечном цикле вводит данные пользователей: имя, затем фамилию, возраст и ID.

Ввод продолжается до тех пор, пока не будет введено пустое поле. Пользователи заносятся в словарь,
где ключ это ID пользователя, а остальные данные записываются в виде кортежа.

Так же программа должна проверять, что:
    * имя и фамилия состоят только из символов и начинаются с большой буквы,
        если не с большой, то заменяет на большую
    * возраст должен быть числом от 18 до 60
    * ID - целое число, дополненное нулями до 8 знаков, ID должен быть уникальным

Дополнительно написать функцию, которая будет выводить полученный словарь в виде таблицы.
"""

ID = str

Info = tuple[str, str, int]
"""Имя, фамилия, возраст."""

Users = dict[ID, Info]


def is_row_literal(row: str) -> bool:
    """Вернёт True, если строка состоит только из букв, иначе False."""
    return all(char.isalpha() for char in row) if row else False


def is_age_correct(value: str) -> bool:
    """Вернёт True, если возраст - целое число в границах от 18 до 60, иначе False."""
    result = all(char.isdigit() for char in value) if value else False

    if result:
        result = 18 <= int(value) <= 60

    return result


def fill_id(value: ID) -> str:
    """Дополнит строку нулями до 8 знаков."""
    if len(value) < 8:
        value = '0' * (8 - len(value)) + value

    return value


def is_id_uniq(users: Users, value: ID) -> bool:
    """Вернёт True, если указанного ключа нет в указанном словаре, иначе False."""
    return not bool(users.get(value)) if value else False


def add_info(id_: ID, info: Info, users: Users) -> None:
    """Добавляет запись в словарь по ключу `id`."""
    users[id_] = info


def display(users: Users):
    """Выводит словарь с юзерами в консоль в виде таблицы."""
    print(head := '{:^10}|{:^20}|{:^20}|{:^5}'.format('ID', 'Name', 'Surname', 'Age'))
    print(line := '-' * len(head))

    for id_, info in users.items():
        print('{:^10}|{:^20}|{:^20}|{:^5}\n{}'.format(id_, *info, line))


def item_added(users: Users) -> bool:
    """Соберет ввод в запись, добавит в словарь, закончит программу, если введут пустую строку."""
    while not is_row_literal(name := input('Введите имя: ')):
        if name == '':
            return False
        print('Имя должно состоять только из букв')

    while not is_row_literal(surname := input('Введите фамилию: ')):
        if surname == '':
            return False
        print('Имя должно состоять только из букв')

    while not is_age_correct(age := input('Введите возраст: ')):
        if age == '':
            return False
        print('Возраст должен быть целым числом в промежутке от 18 до 60')

    while True:
        id_ = input('Введите ID: ')

        if id_ == '':
            return False

        id_ = fill_id(id_)

        if not is_id_uniq(users, id_):
            print('Такой ID уже существует')

        else:
            break

    add_info(id_=id_, info=(name.capitalize(), surname.capitalize(), int(age)), users=users)

    return True


def task4() -> None:
    """Запускает сценарий из описания модуля."""
    users = {}

    while True:
        if not item_added(users):
            break

    if users:
        display(users)

    print('Программа завершена')


if __name__ == '__main__':
    task4()
