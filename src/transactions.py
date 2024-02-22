from functions import *


class Transactions:
    """ Создает экземпляры транзакций. """

    def __init__(self, info):
        self.__info = info

    def is_executed(self) -> bool:
        """Возвращает True если операция успешна. """
        return self.__info.get('state') == 'EXECUTED'

    def get_date(self) -> datetime:
        """ Возвращает дату транзакции. """
        return date_format(self.__info.get('date'))

    def get_date_str(self) -> str:
        """ Возвращает строковое представление даты в нужном формате. """
        return date_show(self.__info.get('date'))

    def get_description(self) -> str:
        """ Возвращает описание транзакции. """
        return self.__info.get('description')

    def get_from_account(self) -> str:
        """ Возвращает счет списания средств."""
        return format_from_account(self.__info.get('from'))

    def get_to_account(self) -> str:
        """ Возвращает счет зачисления средств. """
        return format_to_account(self.__info.get('to'))

    def get_amount(self) -> str:
        """ Возвращает сумму перевода. """
        return self.__info.get('operationAmount').get('amount')

    def get_currency(self) -> str:
        """ Возвращает тип валюты. """
        return self.__info.get('operationAmount').get('currency').get('name')

    def __repr__(self):
        """ Возвращает название класса, Id и дату операции. """
        return (f'Transactions. ID = {self.__info.get('id')}. Date: '
                f'{self.__info.get('date')}')
