import pytest

from task1 import task1
from task3 import task3

task1_test_data = [('545', 5), ('12345', 6), ('012', 3), ('6789', 3)]

task3_test_data = [
    ('aaabbbbccccc', '3a4b5c'),
    ('asssdddsssddd', '1a3s3d3s3d'),
    ('abcba', '1a1b1c1b1a'),
    ('ww aaa   ii i', '2w1 3a3 2i1 1i'),
    ('eee111dd2222...//!!', '3e312d423.2/2!')
]


@pytest.mark.parametrize('input_value, expected_value', task1_test_data)
def test_task1(input_value: str, expected_value: int) -> None:
    assert task1(input_value) == expected_value


@pytest.mark.parametrize('input_value, expected_value', task3_test_data)
def test_task3(input_value: str, expected_value: str) -> None:
    assert task3(input_value) == expected_value
