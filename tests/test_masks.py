import pytest
from src.masks import get_mask_card_number
from src.masks import get_mask_account


def test_get_mask_card_number(number):
    assert get_mask_card_number('2202344354456556') == number


def test_get_mask_account(account_id):
    assert get_mask_account('73654108430135874305') == account_id