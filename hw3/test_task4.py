
import pytest

from task4 import is_row_literal, is_age_correct, fill_id, Users, is_id_uniq, add_info

names_parameters = [('', False), ('John', True), ('M1tch', False), ('Anna Maria', False)]

ages_parameters = [
    ('15', False),
    ('18', True),
    ('25', True),
    ('60', True),
    ('61', False),
    ('', False),
    ('1A', False)
]

id_parameters = [
    ('0', '00000000'),
    ('1', '00000001'),
    ('12', '00000012'),
    ('123', '00000123'),
    ('1234', '00001234'),
    ('12345', '00012345'),
    ('123456', '00123456'),
    ('1234567', '01234567'),
    ('12345678', '12345678'),
    ('123456789', '123456789'),
]

uniq_id_parameters = [('00000000', False), ('123', True)]

users = {
    '00000000': ('Name0', 'Surname0', 50),
    '00000001': ('Name1', 'Surname1', 25),
    '00000002': ('Name2', 'Surname2', 33)
}

additional_users = {'00000003': ('Name3', 'Surname3', 40), '00000004': ('Name4', 'Surname4', 20)}


@pytest.fixture
def default_users() -> Users:
    return users


@pytest.fixture
def updated_users() -> Users:
    result = users.copy()
    result.update(additional_users)

    return result


@pytest.mark.parametrize('input_value, expected_value', names_parameters)
def test_check_name(input_value: str, expected_value: bool) -> None:
    assert is_row_literal(input_value) is expected_value


@pytest.mark.parametrize('input_value, expected_value', ages_parameters)
def test_check_age(input_value: str, expected_value: bool) -> None:
    assert is_age_correct(input_value) is expected_value


@pytest.mark.parametrize('input_value, expected_value', id_parameters)
def test_fill_id(input_value: str, expected_value: str) -> None:
    assert fill_id(input_value) == expected_value


@pytest.mark.parametrize('input_value, expected_value', uniq_id_parameters)
def test_is_id_uniq(input_value: str, expected_value: bool, default_users: Users) -> None:
    assert is_id_uniq(users=default_users, value=input_value) is expected_value


def test_add_info(default_users: Users, updated_users: Users) -> None:
    for key, info in additional_users.items():
        add_info(users=default_users, id_=key, info=info)

    assert default_users == updated_users
