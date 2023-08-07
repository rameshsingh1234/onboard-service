# To Update the entity with status code of 200

# Import the necessary libraries

import requests
from src.unittest.python.utils.read_file import read_headers, read_entities


def test_update_fiu():
    """
    extract the values
    Modify the JSON data to update the entity with new values
    for example : update the ver from 1.0 to 2.0
    Send a PUT request with the updated JSON data to update the entity
    Validate the response status code using assert method
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

    field_to_update = "ver"
    new_value = "2.0"
    if field_to_update in request_body:
        request_body[field_to_update] = new_value

    response = requests.put(api_endpoint, json=request_body, headers=headers)

    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"