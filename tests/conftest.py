import json

import pytest


@pytest.fixture(scope='session')
def json_load():
    with open('operations_copy.json', 'r', encoding='utf-8') as f:
        file = f.read()
        file = json.loads(file)
    return file
