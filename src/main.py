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


def show_transactions():
    """ Выводит 5 крайних успешных транзакций. """
    five_transaction = get_sort_transactions('operations.json')
    count_executed = 0
    count = 0
    while count_executed < 5:
        if five_transaction[count].is_executed():
            print(f'{five_transaction[count].get_date_str()} '
                  f'{five_transaction[count].get_description()}')
            if five_transaction[count].get_from_account() is None:
                print(f'{five_transaction[count].get_to_account()}')
            else:
                print(f'{five_transaction[count].get_from_account()} -> '
                      f'{five_transaction[count].get_to_account()}')
            print(f'{five_transaction[count].get_amount()} '
                  f'{five_transaction[count].get_currency()}\n')
            count_executed += 1
        count += 1


if __name__ == '__main__':
    show_transactions()
