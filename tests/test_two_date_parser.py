import pytest
from functions.two_date_parser import compose_datetime_from


@pytest.mark.parametrize(
    'date_str, time_str, expected_result',
    [
        ('today', '11:55', '2023-03-05 11:55:00'),
        ('tomorrow', '11:55', '2023-03-06 11:55:00'),
        (None, '9:40', '2023-03-05 09:40:00'),
        ('tomorrow', '23:59', '2023-03-06 23:59:00'),
    ]
)
def test_compose_datetime_from(date_str, time_str, expected_result):
    assert str(compose_datetime_from(date_str, time_str)) == expected_result
