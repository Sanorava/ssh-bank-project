import pytest
from src.generators import random_card_number
from src.generators import account_operations

def test_card_number_generator():
    assert next(random_card_number) == '0000 0000 0000 0001'
    assert next(random_card_number) == '0000 0000 0000 0002'
    assert next(random_card_number) == '0000 0000 0000 0003'
    assert next(random_card_number) == '0000 0000 0000 0004'

def test_transaction_descriptions():
    assert next(account_operations) == 'Перевод организации'
    assert next(account_operations) == 'Перевод со счета на счет'
    assert next(account_operations) == 'Перевод со счета на счет'
    assert next(account_operations) == 'Перевод с карты на карту'
