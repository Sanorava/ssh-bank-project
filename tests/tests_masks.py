from src.masks import get_mask_card_number
from src.masks import get_mask_account


assert get_mask_card_number("2202340155662332") == "2202 34** **** 2332"