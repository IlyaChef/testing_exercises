from functions.one_gender import genderalize


def test_genderalize() -> str:
    assert genderalize('сделал', 'сделала', 'male') == 'сделал'
    assert genderalize('унес', 'унесла', 'female') == 'унесла'

