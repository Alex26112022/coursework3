import pytest

from src.transactions import Transactions


@pytest.mark.parametrize('num_transaction, is_executed, date, description, '
                         'from_card, to_account, amount, currency',
                         [(0, True, "26.08.2019",
                           "Перевод организации",
                           "Maestro 1596 83** **** 5199",
                           "Счет **9589",
                           "31957.58",
                           "руб."),
                          (12, False, "12.09.2018",
                           "Перевод организации",
                           "Visa Platinum 1246 37** **** 3588",
                           "Счет **1657",
                           "67314.70",
                           "руб."),
                          (4, True, "04.04.2019",
                           "Перевод со счета на счет",
                           "Счет 1970 86** **** 8542",
                           "Счет **4188",
                           "79114.93",
                           "USD"),
                          (3, True, "23.03.2018",
                           "Открытие вклада",
                           None,
                           "Счет **2431",
                           "48223.05",
                           "руб.")])
def test_transaction(num_transaction, json_load, is_executed, date,
                     description, from_card, to_account, amount, currency):
    """ Проверяет методы класса Transactions. """
    transaction = Transactions(json_load[num_transaction])

    assert transaction.is_executed() == is_executed
    assert transaction.get_date_str() == date
    assert transaction.get_description() == description
    assert transaction.get_from_account() == from_card
    assert transaction.get_to_account() == to_account
    assert transaction.get_amount() == amount
    assert transaction.get_currency() == currency
