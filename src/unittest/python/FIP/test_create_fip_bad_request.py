import pytest
import requests
from src.unittest.python.resources import fip_test_data


@pytest.mark.parametrize(
    "url, client_id, client_secret, user_type, entity_type, request_body, expected_status",
    fip_test_data.fip_invalid_schema)
def test_fip_bad_request(url, client_id, client_secret, user_type, entity_type, request_body, expected_status):
    """
    Extract the values
    Modify the column name in the required field in the JSON data
    For example: name is the required field, change that into names
    Send a POST request with the updated JSON data
    Validate the response status code 400 using the assert method
    :return:-
    """

    api_endpoint = f"{url}/{entity_type}"
    headers = {
        "clientID": client_id,
        "clientSecret": client_secret,
        "userType": user_type
    }

    modified_request_body = request_body.copy()
    if "name" in modified_request_body:
        modified_request_body["names"] = modified_request_body.pop("name")

    response = requests.post(api_endpoint, json=modified_request_body, headers=headers)

    assert response.status_code == expected_status, f"Expected status code {expected_status}, but got {response.status_code},{response.text}"