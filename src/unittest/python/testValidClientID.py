import pytest
import requests
from src.unittest.python.utils.read_file import read_headers, read_entities
from utils.read_file import read_headers


@pytest.fixture
def test_parameters():
    return read_headers


def test_post_client_api(test_parameters):
    """param: test_parameters
     Extract the values using test_parameters
     construct the endpoint
     Add headers and request body
     call the post api
    assert the status code 200
      """

    url = read_headers.get("url")
    version = read_headers.get("version")
    entity_type = read_headers.get("entityType")
    client_id = read_headers.get("clientID")
    client_secret = read_headers.get("clientSecret")
    user_type = read_headers.get("userType")

    api_endpoint = f"{url}/{version}/{entity_type}"
    headers = {
        "clientID": client_id,
        "clientSecret": client_secret,
        "userType": user_type
    }

    request_body = read_entities

    response = requests.post(api_endpoint, json=request_body, headers=headers)

    assert response.status_code == 201, f"Expected status code 201, but got {response.status_code}"
