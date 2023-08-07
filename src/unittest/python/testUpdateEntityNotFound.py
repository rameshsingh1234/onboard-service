# To Update the entity with status code 404

# Import the necessary libraries

import requests
from src.unittest.python.utils.read_file import read_headers, read_entities


def test_update_fiu_same_data():
    """
    extract the values
    Modify the JSON data to update the entity with new values
    for example :updated By passing same data like name is test
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

    updated_field = "name"
    updated_value = "test"

    if updated_field in request_body:
        request_body[updated_field] = updated_value

    response = requests.put(api_endpoint, json=request_body, headers=headers)

    assert response.status_code == 404, f"Expected status code 404, but got {response.status_code}"
