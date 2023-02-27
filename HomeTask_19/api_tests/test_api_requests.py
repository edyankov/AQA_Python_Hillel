"""Створити кілька реальних API тестів на https://reqres.in/: отримати методом GET кілька користувачів, отримати методом
GET одного користувача, пройти авторизацію за допомогою метода GET, створити персону з допомогою метода POST"""

import pytest
import json
import requests


class TestApi:

    @pytest.mark.apitest
    def test_get_users(self):
        url = 'https://reqres.in/api/users?page=2'
        response = requests.get(url)
        assert response.status_code == 200
        users_data = json.loads(response.text).get('data')
        print(users_data)

    @pytest.mark.apitest
    def test_get_user(self):
        url = 'https://reqres.in/api/users/9'
        response = requests.get(url)
        u_data = json.loads(response.text).get('data').get('id')
        assert u_data == 9
        print(response.text)

    @pytest.mark.apitest
    def test_authorization(self):
        url = 'https://reqres.in/api/login'
        body = {
                "email": "eve.holt@reqres.in",
                "password": "cityslicka"
            }
        response = requests.post(url, json=body)
        assert response.status_code == 200
        print(response.text)

    @pytest.mark.apitest
    def test_create_person(self):
        url = 'https://reqres.in/api/users'
        body = {
            "name": "morpheus",
            "job": "leader"
        }
        response = requests.post(url, json=body)
        assert response.status_code == 201
        print(response.text)
