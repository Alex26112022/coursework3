import pytest
from coursework3.functions import *


def test_load_json():
    """ Проверка соответствия типа загружаемых данных. """
    assert type(load_json('operations_copy.json')) == list
    assert type(load_json('operations_copy.json')[0]) == dict
