#Committed Code 2 times

import pytest
import requests
import json
# run: pytest <module_name.py>


def main_url():
    return 'https://reqres.in'


def test_valid_login():
    url = main_url() + "/api/login/"
    data = {'email': 'eve.holt@reqres.in', 'password': 'cityslicka'}
    response = requests.post(url, data=data)
    token = json.loads(response.text)
    assert response.status_code == 200
    assert token['token'] == 'QpwL5tke4Pnpja7X4'