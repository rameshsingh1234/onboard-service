# validate Ip is added in the aure WAF by passing corret ip

# Import the necessary libraries

import requests
from src.unittest.python.utils.read_file import read_headers, read_entities


def test_validate_ipaddress():
    """
    Send a POST request with the valid JSON data
    Check if the IP is added in the response
    Validate the response status code and message
    """
    url = read_headers.get("url")
    version = read_headers.get("version")
    entity_type = read_headers.get("entityType")
    client_id = read_headers.get("clientID")
    client_secret = read_headers.get("clientSecret")
    user_type = read_headers.get("userType")
    expected_ip = read_headers.get("expectedIP")

    api_endpoint = f"{url}/{version}/{entity_type}"
    headers = {
        "clientID": client_id,
        "clientSecret": client_secret,
        "userType": user_type
    }

    request_body = read_entities

    response = requests.post(api_endpoint, json=request_body, headers=headers)
    response_data = response.json()
    added_ip = response_data.get("ip")
    assert added_ip == expected_ip, f"Expected IP {expected_ip}, but got {added_ip}"
