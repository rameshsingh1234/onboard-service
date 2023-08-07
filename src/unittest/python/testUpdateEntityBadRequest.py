# To Update the entity with status code 400
import pytest
# Import the necessary libraries

import requests
from src.unittest.python.utils.read_file import read_headers, read_entities




def test_update_fiu_bad_request():
    """
    extract the values
    Modify the JSON data to update the entity with new values
    for example: update the entity type in headers with invalid values
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

    invalid_entity_type = "AAFIU"
    new_headers = headers.copy()
    new_headers["entityType"] = invalid_entity_type

    response = requests.put(api_endpoint, json=read_entities, headers=new_headers)

    assert response.status_code == 400, f"Expected status code 200, but got {response.status_code}"
