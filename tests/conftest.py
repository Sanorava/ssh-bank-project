import pytest


@pytest.fixture()
def number():
    return '4132 13** **** 3482'


@pytest.fixture()
def account_id():
    return '**4305'


@pytest.fixture()
def account_number():
    return 'Счёт **1111'


@pytest.fixture()
def account_card():
    return 'Visa Platinum 7000 79** **** 6361'


@pytest.fixture()
def get_data():
    return '11.03.2024'


@pytest.fixture()
def my_list():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]


@pytest.fixture()
def card_number():
    return 1, 9999999999999999
