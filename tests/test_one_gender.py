import pytest
from functions.one_gender import genderalize

@pytest.mark.parametrize(
    'verb_male, verb_female, gender, expected_result',
    [
        ('verb_male', 'verb_female', 'male', 'verb_male'),
        ('verb_male', 'verb_female', 'female', 'verb_female'),
    ],
)


def test_genderalize(verb_male, verb_female, gender, expected_result):
    assert genderalize(verb_male, verb_female, gender) == expected_result


