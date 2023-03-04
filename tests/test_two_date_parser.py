import pytest
from functions.two_date_parser import compose_datetime_from


@pytest.mark.parametrize(
    'date_str, time_str, expected_result',
    [
        ('today', '11:55', '2023-03-04 11:55:00'),
        ('tomorrow', '11:55', '2023-03-05 11:55:00'),
    ],
)


def test_compose_datetime_from(date_str, time_str, expected_result):
    assert str(compose_datetime_from(date_str, time_str)) == expected_result
