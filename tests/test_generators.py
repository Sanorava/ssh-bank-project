import pytest
from src.generators import random_card_number

def test_card_number_generator():
    assert next(random_card_number) == '0000 0000 0000 0001'
    assert next(random_card_number) == '0000 0000 0000 0002'
    assert next(random_card_number) == '0000 0000 0000 0003'
    assert next(random_card_number) == '0000 0000 0000 0004'