import pytest
import json
import requests


class TestApiReqres:

    # @pytest.mark.api
    def test_get_users(self):
        url = 'https://reqres.in/api/users?page=2'
        response = requests.get(url)
        assert response.status_code == 200
        data = json.loads(response.text).get('data')
        print(len(data))

    # @pytest.mark.api
    def test_get_user(self):
        url = 'https://reqres.in/api/users/9'
        response = requests.get(url)
        data = json.loads(response.text).get('data').get('id')
        assert data == 9

    # @pytest.mark.api
    def test_authorization(self):
        url = 'https://reqres.in/api/login'
        body = {
                "email": "eve.holt@reqres.in",
                "password": "pistol"
            }
        response = requests.get(url, json=body)
        assert response.status_code == 200
        print(response.text)

    # @pytest.mark.api
    def test_create_person(self):
        url = 'https://reqres.in/api/users'
        body = {
            "name": "morpheus",
            "job": "leader"
        }
        response = requests.post(url, json=body)
        assert response.status_code == 201
