import pytest
from src.masks import get_mask_card_number
from src.masks import get_mask_account


def test_get_mask_card_number(number):
    assert get_mask_card_number('4132138567073482') == number


def test_get_mask_account(account_id):
    assert get_mask_account('73654108430135874305') == account_id


@pytest.mark.parametrize('card_number, expected', [('2202344354456556', '2202 34** **** 6556'),
                         ('2202455467789021', '2202 45** **** 9021')])


def test_masked_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected
