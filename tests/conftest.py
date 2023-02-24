import pytest



@pytest.fixture
def verb_male():
    return 'накодил'


@pytest.fixture
def verb_female():
    return 'накодила'


@pytest.fixture
def host_name():
    return 'https://www.avito.ru'


@pytest.fixture
def relative_url():
    return 'moskva_i_mo/nedvizhimost'


@pytest.fixture
def get_params():
    return {'localPriority': '0', 'q': 'дом'}
