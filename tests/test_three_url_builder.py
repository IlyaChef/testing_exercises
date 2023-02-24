import pytest
from typing import Mapping
from functions.three_url_builder import build_url

@pytest.mark.parametrize(
    'host_name, relative_url, get_params, expected_result',
    [
        ('https://www.avito.ru', 'moskva_i_mo/nedvizhimost', {'localPriority': '0', 'q': 'дом'}, 'https://www.avito.ru/moskva_i_mo/nedvizhimost?localPriority=0&q=дом'),
    ],
)

def test_build_url(host_name, relative_url, get_params: Mapping[str, str], expected_result: str):
    assert build_url(host_name, relative_url, get_params) == expected_result
