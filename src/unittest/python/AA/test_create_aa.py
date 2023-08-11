import pytest
import requests
from src.unittest.python.resources import aa_test_data


@pytest.mark.parametrize(
    "url, client_id, client_secret, user_type, entity_type, request_body, expected_status",
    aa_test_data.aa_create_schema)
def test_create_aa(url, client_id, client_secret, user_type, entity_type, request_body, expected_status):
    """
    Send a POST request with the valid JSON data.
    Validate the response status code and message
    :return:
    """

    api_endpoint = f"{url}/{entity_type}"
    headers = {
        "clientID": client_id,
        "clientSecret": client_secret,
        "userType": user_type
    }

    response = requests.post(api_endpoint, json=request_body, headers=headers)

    assert response.status_code == expected_status, f"Expected status code {expected_status}, but got {response.status_code},{response.text}"
