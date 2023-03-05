import pytest
from typing import Mapping
from functions.three_url_builder import build_url

@pytest.mark.parametrize(
    'host_name, relative_url, get_params, expected_result',
    [
        (
            'https://www.avito.ru',
            'moskva_i_mo/nedvizhimost',
            {'localPriority': '0', 'q': 'дом'},
            'https://www.avito.ru/moskva_i_mo/nedvizhimost?localPriority=0&q=дом'
        ),
        (
            'https://www.avito.ru',
            'moskva/igry_pristavki_i_programmy',
            None,
            'https://www.avito.ru/moskva/igry_pristavki_i_programmy'
        ),
        (
            'https://www.google.com',
            'search',
            {'q': 'reddit+api+python', 'num': '9'},
            'https://www.google.com/search?q=reddit+api+python&num=9',
        ),
        (
            'https://github.com',
            'praw-dev/praw/blob/master',
            {'path': 'README.rst'},
            'https://github.com/praw-dev/praw/blob/master?path=README.rst'
        ),
    ],
)
def test_build_url(host_name, relative_url, get_params: Mapping[str, str], expected_result: str):
    assert build_url(host_name, relative_url, get_params) == expected_result
