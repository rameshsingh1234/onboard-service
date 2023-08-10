import pytest
import requests
from src.unittest.python.resources import fiu_test_data


@pytest.mark.parametrize(
    "url, client_id, client_secret, user_type, entity_type, request_body, expected_status",
    fiu_test_data.fiu_create_entity_exist_schema)
def test_fiu_exist(url, client_id, client_secret, user_type, entity_type, request_body, expected_status):
    """
    Send a POST request with the provided JSON data
    Validate the response status code
    Extract the ID in the Entityinfo column from the response for later use
    Send another POST request with the updated JSON data with the same ID to create the entity again
    Validate the second response status code and message
    :return:
    """
    api_endpoint = f"{url}/{entity_type}"
    headers = {
        "clientID": client_id,
        "clientSecret": client_secret,
        "userType": user_type
    }

    # First request to create the entity
    response = requests.post(api_endpoint, json=request_body, headers=headers)

    assert response.status_code == 201, f"Expected status code 201, but got {response.status_code},{response.text},{response.text}"

    # Extract the entity ID from the request body
    entity_id = request_body.get("entityinfo", {}).get("id")

    # Second request to create the entity again with the same ID
    updated_request_body = request_body.copy()
    updated_request_body["entityinfo"]["id"] = entity_id

    second_response = requests.post(api_endpoint, json=updated_request_body, headers=headers)

    # Check the second response status code and message
    assert second_response.status_code == 409, f"Expected status code 409, but got {second_response.status_code},{response.text}"
