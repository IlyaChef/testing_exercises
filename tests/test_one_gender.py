import pytest
from functions.one_gender import genderalize

@pytest.mark.parametrize(
    'verb_male, verb_female, gender, expected_result',
    [
        ('накодил', 'накодила', 'male', 'накодил'),
        ('накодил', 'накодила', 'female', 'накодила'),
    ],
)


def test_genderalize(verb_male, verb_female, gender, expected_result):
    assert genderalize(verb_male, verb_female, gender) == expected_result


