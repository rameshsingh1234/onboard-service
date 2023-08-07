# To validate the invalid clientID with 400

# Import the necessary libraries

import requests
from src.unittest.python.utils.read_file import read_headers, read_entities


def test_invalid_client_id():
    """
    extract the values
    Modify the clientID from the headers
    Send a post request with the updated JSON data and the headers
    Validate the response status code 400 using assert method
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

    new_client_id = "abc123"
    headers["clientID"] = new_client_id

    response = requests.post(api_endpoint, json=request_body, headers=headers)

    assert response.status_code == 400, f"Expected status code 400, but got {response.status_code}"
