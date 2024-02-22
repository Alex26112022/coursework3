from datetime import datetime

from src.main import get_sort_transactions


def test_get_sort_transactions():
    """ Проверяет типы возвращаемых данных всех методов всех экземпляров. """
    count_none_account = 0
    count_executed = 0
    test_list = get_sort_transactions('operations_copy.json')
    for el in test_list:
        if el.is_executed():
            count_executed += 1
        assert type(el.is_executed()) is bool
        assert type(el.get_date()) is datetime
        assert type(el.get_date_str()) is str
        assert type(el.get_description()) is str
        if bool(el.get_from_account()) is False:
            count_none_account += 1
        else:
            assert type(el.get_from_account()) is str
        assert type(el.get_to_account()) is str
        assert type(el.get_amount()) is str
        assert type(el.get_currency()) is str
    print(f'Всего транзакций: {len(test_list)}')
    print(f'Успешных транзакций: {count_executed}')
    print(f'Отсутствующих счетов списания: {count_none_account}')
