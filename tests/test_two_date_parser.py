import pytest
from functions.two_date_parser import compose_datetime_from


@pytest.mark.parametrize(
    'date_str, time_str, expected_result',
    [
    ('today', '22:55', '2023-02-23 22:55:00'),
    ('tomorrow', '22:55', '2023-02-24 22:55:00'),
    ],
)

def test_compose_datetime_from(date_str, time_str, expected_result):
    assert str(compose_datetime_from(date_str, time_str)) == expected_result


