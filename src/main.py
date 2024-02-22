from functions import load_json
from transactions import Transactions


def get_sort_transactions(json_path) -> list:
    """ Возвращает отсортированный по датам список экземпляров класса
    Transactions с успешными транзакциями. """
    all_information = load_json(json_path)

    list_transactions = []
    for el in all_information:
        if bool(el):
            list_transactions.append(Transactions(el))

    list_transactions.sort(key=lambda transaction: transaction.get_date(),
                           reverse=True)

    return list_transactions
