import pytest
from functions.five_title import change_copy_item


@pytest.mark.parametrize(
    'title, expected_result',
    [
        ("The quick brown fox jumps over the lazy dog", "Copy of The quick brown fox jumps over the lazy dog"),
        ("Copy of The quick brown fox jumps over the lazy dog",
         "Copy of The quick brown fox jumps over the lazy dog (2)"),
        (
        "An inspired calligrapher can create pages of beauty using stick ink, quill, brush, pick-axe, buzz saw, or even strawberry jam",
        "An inspired calligrapher can create pages of beauty using stick ink, quill, brush, pick-axe, buzz saw, or even strawberry jam"),
    ]
)


def test_change_copy_item(title, expected_result):
    assert change_copy_item(title) == expected_result
