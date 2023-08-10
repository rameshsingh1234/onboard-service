import pytest
import requests
from src.unittest.python.utils.read_file import read_headers, read_entities
from src.unittest.python.resources import fiu_test_data  # Import your test data file


# Modify the data structure to match the number of parameter names
@pytest.mark.parametrize(
    "url, client_id, client_secret, user_type, entity_type, request_body, expected_status",
    fiu_test_data.fiu_invalid_schema)
def test_fiu_bad_request(url, client_id, client_secret, user_type, entity_type, request_body, expected_status):
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

    # Modify the request_body as needed, e.g., changing "name" to "names"
    modified_request_body = request_body.copy()
    if "name" in modified_request_body:
        modified_request_body["names"] = modified_request_body.pop("name")

    response = requests.post(api_endpoint, json=modified_request_body, headers=headers)

    # Check the response status code matches the expected status
    assert response.status_code == expected_status, f"Expected status code {expected_status}, but got {response.status_code},{response.text}"

# # To create an entity with status code 400
#
# # Import the necessary libraries
#
# import requests
# from src.unittest.python.utils.read_file import read_headers, read_entities
#
#
# def test_create_fiu_bad_request():
#     """
#     extract the values
#     Modify the column name in the required field in the json data
#     for example : name is the required field change that into names
#     Send a post request with the updated JSON data
#     Validate the response status code 400 using assert method
#     :return:
#     """
#
#     url = read_headers.get("url")
#     version = read_headers.get("version")
#     entity_type = read_headers.get("entityType")
#     client_id = read_headers.get("clientID")
#     client_secret = read_headers.get("clientSecret")
#     user_type = read_headers.get("userType")
#
#     api_endpoint = f"{url}/{version}/{entity_type}"
#     headers = {
#         "clientID": client_id,
#         "clientSecret": client_secret,
#         "userType": user_type
#     }
#
#     request_body = read_entities
#
#     # Check if "requester" exists in the request_body dictionary and remove it
#     if "requester" in request_body:
#         del request_body["requester"]
#
#     response = requests.post(api_endpoint, json=request_body, headers=headers)
#
#     # Check the response status code is 400 as expected
#     assert response.status_code == 400, f"Expected status code 400, but got {response.status_code},{response.text}"
