import pytest
import requests


def test_response_status_code(shared_variable):
    base_url = shared_variable["BASE_URL"]
    response = requests.get(base_url)
    assert response.status_code == 200


def test_response_json_key_and_value(shared_variable):
    base_url = shared_variable["BASE_URL"]
    response = requests.get(base_url)
    response_json = response.json()
    assert "characters" in response_json
    assert "locations" in response_json
    assert "episodes" in response_json
    assert base_url + "/character" in response.text
    assert base_url + "/location" in response.text
    assert base_url + "/episode" in response.text


def test_api_response_header(shared_variable):
    base_url = shared_variable["BASE_URL"]
    response = requests.get(base_url)
    assert "X-Nf-Request-Id" in response.headers
    assert "Content-Type" in response.headers
