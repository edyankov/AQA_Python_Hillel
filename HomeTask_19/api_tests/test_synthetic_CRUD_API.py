"""API tests: Створити по одному синтетичному API тесту, для кожної функції CRUD (Create, read, update, delete). """

import pytest
import requests

TEST_URL = "http://localhost:3000"


@pytest.fixture
def setup_data():
    data = {"name": "John", "email": "john@example.com"}
    response = requests.post(TEST_URL + "/users", json=data)
    assert response.status_code == 201
    data["id"] = response.json()["id"]
    yield data


def test_create(setup_data):
    data = {"name": "Jane", "email": "jane@example.com"}
    response = requests.post(TEST_URL + "/users", json=data)
    assert response.status_code == 201


def test_read(setup_data):
    response = requests.get(TEST_URL + "/users/" + str(setup_data["id"]))
    assert response.status_code == 200


def test_update(setup_data):
    data = {"name": "John Doe", "email": "johndoe@example.com"}
    response = requests.put(TEST_URL + "/users/" + str(setup_data["id"]), json=data)
    assert response.status_code == 200


def test_delete(setup_data):
    response = requests.delete(TEST_URL + "/users/" + str(setup_data["id"]))
    assert response.status_code == 204
