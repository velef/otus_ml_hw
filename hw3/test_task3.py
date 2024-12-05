import pytest
from task3 import is_digit, is_simple

is_digit_reference = [
    ('100', True),
    ('0', True),
    ('10.0', False),
    ('-1', False),
    ('', False),
    ('A1', False),
]

is_simple_reference = [
    (-1, False),
    (0, False),
    (1, False),
    (2, True),
    (17, True),
    (20, False),
    (23, True),
    (97, True),
    (158, False),
]


@pytest.mark.parametrize('input_value, expected_value', is_digit_reference)
def test_is_digit(input_value, expected_value):
    assert is_digit(input_value) is expected_value


@pytest.mark.parametrize('input_value, expected_value', is_simple_reference)
def test_is_simple(input_value, expected_value):
    assert is_simple(input_value) is expected_value
