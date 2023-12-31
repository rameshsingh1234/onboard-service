import requests
import json
from src.unittest.python.utils import read_file
import os


class Keycloak:

    def __init__(self, conf):
        self.conf = conf

    def get_token(self, client_id, client_secret):
        """Generates a Keycloak token with the client credential flow.

          Args:
            client_id: The client ID.
            client_secret: The client secret.

          Returns:
            The token, or None if the token could not be generated.
          """

        url = f"{self.conf.get('keycloak_base_url')}/realms/{self.conf.get('realm')}/protocol/openid-connect/token"
        print(url)
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        data = {
            "grant_type": "client_credentials",
            "client_id": client_id,
            "client_secret": client_secret
        }
        response = requests.post(url, headers=headers, data=data)
        if response.status_code == 200:
            token = json.loads(response.content)["access_token"]
            return token
        else:
            # print("Failed to generate token: {}".format(response.status_code))
            return response.status_code, response.text

    def create_client(self, access_token, entity_id, base_url):
        """
           Creates a new client instance using the provided access token and entity ID.

           Args:
               access_token (str): The access token used to authenticate the client.
               entity_id (str): The entity id is used as client id.
               base_url (str): base url

           Returns:
               Client: A new client  with the provided access token and entity ID, returns clientId and secret.
           """

        url = f"{self.conf.get('keycloak_base_url')}/admin/realms/{self.conf.get('realm')}/clients"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}"}

        fiu_template = self.conf.get('fiu_keycloak_client_template_filename')
        payload = read_file.read_data(os.path.join(os.path.dirname(__file__), 'resources/templates', fiu_template))
        payload['clientId'] = entity_id
        payload['redirectUris'].clear()
        payload['redirectUris'].append(base_url)

        response = requests.request("POST", url, headers=headers, data=json.dumps(payload))
        print("response::::", response.status_code, response.text)
        if response.status_code == 201:
            url = f"{self.conf.get('keycloak_base_url')}/admin/realms/{self.conf.get('realm')}/clients"
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {access_token}"}

            response = requests.request("GET", url, headers=headers, data=payload)

            if response.status_code == 200:
                for clients in response.json():
                    if "clientId" in clients and clients["clientId"] == entity_id:
                        return {"clientId": clients.get('clientId'),
                                "secret": clients.get('secret')}
                return False
            else:
                # fail to get clients from keycloak
                return False
        else:
            # fail to create client in keycloak
            return False
            # fetch the client_id and secret and return
