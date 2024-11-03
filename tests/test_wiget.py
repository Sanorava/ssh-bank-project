import pytest
from src.wiget import mask_account_card
from src.wiget import get_date


def test_mask_account_card(account_number):
    assert mask_account_card('Счёт 11111111111111111111') == account_number
    assert mask_account_card('Счет 11111111111111111111') == 'Счет **1111'


def test_mask_account_card_number(account_card):
    assert mask_account_card('Visa Platinum 7000792289606361') == account_card
    assert mask_account_card('Visa Gold 7000792289606361') == 'Visa Gold 7000 79** **** 6361'
    assert mask_account_card('Maestro 7000792289606361') == 'Maestro 7000 79** **** 6361'


def test_get_date(get_data):
    assert get_date("2024-03-11T02:26:18.671407") == get_data
    assert get_date("2024-11-12T11:45:10.671407") == '12.11.2024'


@pytest.mark.parametrize('date, expected', [("2023-06-10T02:26:18.671407", '10.06.2023'),
                                            ("2024-01-19T02:26:18.671407", '19.01.2024')])


def test_get_date(date, expected):
    assert get_date(date) == expected
