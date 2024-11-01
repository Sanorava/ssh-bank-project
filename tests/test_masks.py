import pytest
from src.masks import get_mask_card_number
from src.masks import get_mask_account


assert get_mask_card_number('2202344354456556') == '2202 34** **** 5655'
assert get_mask_account('111111111111111111111') == '**11111'