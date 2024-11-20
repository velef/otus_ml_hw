
import pytest

from task1 import is_snake_case, is_camel_case, to_camel_case, to_snake_case, convert


is_snake_case_parameters = [('is_snake_case', True), ('IsSnakeCase', False)]
is_camel_case_parameters = [('is_snake_case', False), ('IsSnakeCase', True)]
to_camel_case_reference = [('is_snake_case', 'IsSnakeCase')]
to_snake_case_reference = [('IsSnakeCase', 'is_snake_case')]
convert_reference = [('is_snake_case', 'IsSnakeCase'), ('IsSnakeCase', 'is_snake_case')]


@pytest.mark.parametrize('input_value, expected_value', is_snake_case_parameters)
def test_is_snake_case(input_value, expected_value) -> None:
    assert is_snake_case(input_value) == expected_value


@pytest.mark.parametrize('input_value, expected_value', is_camel_case_parameters)
def test_is_camels_case(input_value, expected_value) -> None:
    assert is_camel_case(input_value) == expected_value


@pytest.mark.parametrize('input_value, expected_value', to_snake_case_reference)
def test_to_snake_case(input_value, expected_value) -> None:
    assert to_snake_case(input_value) == expected_value


@pytest.mark.parametrize('input_value, expected_value', to_camel_case_reference)
def test_to_camel_case(input_value, expected_value) -> None:
    assert to_camel_case(input_value) == expected_value


@pytest.mark.parametrize('input_value, expected_value', convert_reference)
def test_convertor(input_value, expected_value) -> None:
    assert convert(input_value) == expected_value
