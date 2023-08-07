# To create an entity with status code 200

# Import the necessary libraries

import requests
from src.unittest.python.utils.read_file import read_headers, read_entities


def test_create_fiu():
    """
    Send a POST request with the valid JSON data
    Validate the response status code and message
    :return:
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

    assert response.status_code == 201, f"Expected status code 200, but got {response.status_code}"