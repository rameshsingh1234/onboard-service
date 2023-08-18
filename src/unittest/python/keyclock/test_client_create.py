import os

import pytest
from src.main.python.Keycloak import Keycloak
from src.unittest.python.utils import read_config_file

# Read test headers from JSON
# with open('testHeaders.json', 'r') as file:
#     test_headers = json.load(file)

test_headers = read_config_file.read_config(
    os.path.join(os.path.dirname(os.path.dirname(__file__)), "resources", "testHeaders.json"))


# Test cases using pytest.mark.parametrize
@pytest.mark.parametrize("client_id, client_secret, base_url", [
    (test_headers["client_id"], test_headers["client_secret"], test_headers["url"]),
])
def test_create_client(client_id, client_secret, base_url):
    keycloak = Keycloak(test_headers)

    result = keycloak.create_client("mock_access_token", client_id, base_url)
    expected_result = {"clientId": client_id, "secret": "mock_secret"}

    assert result == expected_result


if __name__ == "__main__":
    pytest.main(["-v", "test_keycloak.py"])
