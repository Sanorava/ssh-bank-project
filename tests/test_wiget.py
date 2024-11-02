import pytest
from src.wiget import mask_account_card
from src.wiget import get_date

assert mask_account_card('Счёт 11111111111111111111') == 'Счёт **1111'
assert mask_account_card('Счет 11111111111111111111') == 'Счет **1111'
assert mask_account_card('Visa Platinum 7000792289606361') == 'Visa Platinum 7000 79** **** 0636'
assert mask_account_card('Visa Gold 7000792289606361') == 'Visa Gold 7000 79** **** 0636'
assert mask_account_card('Maestro 7000792289606361') == 'Maestro 7000 79** **** 0636'


assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"
