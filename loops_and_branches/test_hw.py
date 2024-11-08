import pytest

from task1 import compress_to_single as task1
from task2 import check_seats as task2
from task3 import compress_using_rle as task3
from task4 import encrypt_using_caesar as task4

task1_test_data = [('545', 5), ('12345', 6), ('012', 3), ('6789', 3)]

task2_test_data = [
    ([[0, 1, 1, 0], [1, 0, 0, 0], [0, 1, 0, 0]], 2, 1),
    ([[0, 1, 1, 0], [1, 0, 0, 0], [0, 1, 0, 0]], 0, False),
    ([[0, 1, 1, 0], [1, 0, 1, 0], [1, 1, 0, 1]], 2, False),
    ([[0, 1, 1, 0], [1, 0, 1, 0], [1, 1, 0, 1]], 1, 0),
    ([[0, 0, 0, 0, 0, 0]], 5, 0),
    ([[0, 0, 0, 0, 1, 0]], 5, False),
    ([[0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0]], 5, 1),
    ([[0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0]], 3, 0),
]

task3_test_data = [
    ('aaabbbbccccc', '3a4b5c'),
    ('asssdddsssddd', '1a3s3d3s3d'),
    ('abcba', '1a1b1c1b1a'),
    ('ww aaa   ii i', '2w1 3a3 2i1 1i'),
    ('eee111dd2222...//!!', '3e312d423.2/2!')
]

task4_test_data = [
    ('Dog', 2, 'Fqi'),
    ('Zak zak', 3, 'Cdn cdn'),
    ('Python is the BEST', 5, 'Udymts nx ymj GJXY'),
    ('abcdefjhijklmnopqrstuvwxyz', 1, 'bcdefgkijklmnopqrstuvwxyza'),
    ('ABCDEFJHIJKLMNOPQRSTUVWXYZ', 2, 'CDEFGHLJKLMNOPQRSTUVWXYZAB'),
    ('Привет!', 3, 'Привет!'),
    (
        'Caesar shift is one of the simplest and most widely known encryption techniques.',
        20,
        'Wuymul mbczn cm ihy iz nby mcgjfymn uhx gimn qcxyfs ehiqh yhwlsjncih nywbhckoym.'
    ),
    ('Cipher Disk 2000', 40, 'Rxewtg Sxhz 2000'),
    ('word', 0, 'word'),
    ('', 11, '')
]


@pytest.mark.parametrize('input_value, expected_value', task1_test_data)
def test_task1(input_value: str, expected_value: int) -> None:
    assert task1(input_value) == expected_value


@pytest.mark.parametrize('rows, tickets_amount, expected_value', task2_test_data)
def test_task2(rows: list[list[int]], tickets_amount: int, expected_value: int or bool) -> None:
    assert task2(rows, tickets_amount) == expected_value


@pytest.mark.parametrize('input_value, expected_value', task3_test_data)
def test_task3(input_value: str, expected_value: str) -> None:
    assert task3(input_value) == expected_value


@pytest.mark.parametrize('input_value, key, expected_value', task4_test_data)
def test_task4(input_value: str, key: int, expected_value: int) -> None:
    assert task4(input_value, key) == expected_value
