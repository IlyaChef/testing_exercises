from functions.four_bank_parser import parse_ineco_expense


def test_parse_ineco_expense(sms_message, bank_cards, expected_expense):
    assert parse_ineco_expense(sms_message, bank_cards) == expected_expense
