# validate Ip is added in the aure WAF by passing incorrect ip  with status code 404

# Import the necessary libraries

import requests
from src.unittest.python.utils.read_file import read_headers, read_entities


def test_invalid_ipaddress():
    """
    extract the values
    Modify the ips in the Entityinfo column from the response for later use
    Send a post request with the updated JSON data
    Validate the response status code 404 using assert method
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
    for entity in request_body:
        entity['Entityinfo']['ip'] = "invalid_ip_address"

    response = requests.post(api_endpoint, json=request_body, headers=headers)

    assert response.status_code == 404, f"Expected status code 404, but got {response.status_code}"
