import datetime
import decimal
import pytest
from functions.four_bank_parser import BankCard, SmsMessage, Expense


@pytest.fixture
def verb_male():
    return 'накодил'


@pytest.fixture
def verb_female():
    return 'накодила'



@pytest.fixture
def bank_cards() -> list[BankCard]:
    return [
        BankCard(last_digits='6869', owner='Ilya'),
        BankCard(last_digits='4321', owner='Anna'),
    ]


@pytest.fixture
def sms_message() -> SmsMessage:
    return SmsMessage(
            text='47.00 RUB, 1234999922226869 04.03.23 12:00 PYATEROCHKA authcode 0123',
            author='RAIFFEISEN',
            sent_at=datetime.datetime(2023, 3, 4, 12, 0),
        )


@pytest.fixture
def expected_expense(bank_cards) -> Expense:
    return Expense(
            amount=decimal.Decimal('47.00'),
            card=bank_cards[0],
            spent_in='PYATEROCHKA',
            spent_at=datetime.datetime(2023, 3, 4, 12, 0),
        )
