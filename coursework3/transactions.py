from functions import *


class Transactions:
    """ Создает экземпляры транзакций. """

    def __init__(self, info):
        self.__info = info

    def is_executed(self) -> bool:
        """Возвращает True если операция успешна. """
        pass

    def get_date(self) -> datetime:
        """ Возвращает дату транзакции. """
        pass

    def get_date_str(self) -> str:
        """ Возвращает строковое представление даты в нужном формате. """
        pass

    def get_description(self) -> str:
        """ Возвращает описание транзакции. """
        pass

    def get_from_account(self) -> str:
        """ Возвращает счет списания средств."""
        pass

    def get_to_account(self) -> str:
        """ Возвращает счет зачисления средств. """
        pass

    def get_amount(self) -> str:
        """ Возвращает сумму перевода. """
        pass

    def get_currency(self) -> str:
        """ Возвращает тип валюты. """
        pass

    def __repr__(self):
        """ Возвращает название класса, Id и дату операции. """
        pass
