import os
from src.main.python.Keycloak import Keycloak
from src.unittest.python.utils import read_config_file

# Read the 'conf' dictionary from the testHeaders.json file
conf = read_config_file.read_config(
    os.path.join(os.path.dirname(os.path.dirname(__file__)), "resources", "testHeaders.json"))


def test_create_client_success():
    keycloak = Keycloak(conf)
    client_id = conf.get("client_id")
    client_secret = conf.get("client_secret")
    entity_id = conf.get("entity_id")
    keycloak_base_url = conf.get("keycloak_base_url")

    # Obtain the access token using the get_token method
    access_token = keycloak.get_token(client_id, client_secret)

    result = keycloak.create_client(access_token, entity_id, keycloak_base_url)

    assert result is not False
    assert "clientId" in result
    assert "secret" in result
    assert result["clientId"] == entity_id
