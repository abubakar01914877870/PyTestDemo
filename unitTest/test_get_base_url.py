import pytest
import requests


def test_API_GET_Status_Code(shared_variable):
    url = shared_variable["BASE_URL"]
    response = requests.get(url)
    assert response.status_code == 200


def test_json_key_and_value(shared_variable):
    base_url = shared_variable["BASE_URL"]
    response = requests.get(base_url)
    response_json = response.json()
    assert "characters" in response_json
    assert "locations" in response_json
    assert "episodes" in response_json
    assert base_url + "/character" in response.text
    assert base_url + "/location" in response.text
    assert base_url + "/episode" in response.text



def test_ass():
    print("I am inside test")
    assert 2 + 2 == 4

