import pytest
from src.generators import card_number_generator

def test_card_number_generator(card_number):
    assert card_number_generator(1, 9999999999999999) == card_number