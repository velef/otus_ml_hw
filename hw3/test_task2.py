import pytest
from task2 import is_input_format_correct, validate_date

input_format_validation = [('01.12.2024', True), ('01-12.2024', False), ('1.12.2024', False)]
validate_date_reference = [('29.02.2000', True), ('29.02.2001', False), ('31.04.1962', False)]


@pytest.mark.parametrize('input_date, expected_value', input_format_validation)
def test_check_input_date_format(input_date, expected_value) -> None:
    assert is_input_format_correct(input_date) is expected_value


@pytest.mark.parametrize('input_date, expected_value', validate_date_reference)
def test_validate_date(input_date, expected_value) -> None:
    assert validate_date(input_date) is expected_value
