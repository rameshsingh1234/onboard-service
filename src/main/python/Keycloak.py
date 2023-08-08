# import necessary libraries
import time

import jwt as jwt
# import pycryptodome.jwt.algorithms

import requests
import json


# VKWZNwLdnfC6Izh2vdt0UgIlEkPzRynl
class Keycloak:
    def __init__(self, conf):
        self.conf = conf

    def read_client_id(self):
        """
        Read the clientID from the Config file
        call the keycloak get client api
        return clientID (set of response)
        compare the both the client id's
        condition is true 200 ok response
        else specific messages with response code
        """

    def get_token(self, client_id, client_secret):
        """
        call the keycloak post method api
        in header pass clientId and secrete
        hit the api to get the access token
        """

        """Generates a Keycloak token with the client credential flow.

          Args:
            client_id: The client ID.
            client_secret: The client secret.
            realm: The realm name.

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
            print("Failed to generate token: {}".format(response.status_code))
            return None

    def create_client(self):
        """
        call the post method create client keycloak api
        header: application/json
        Authorization: AccessToken
        request body:
        :return:
        """
        # create access-token
        # call /admin/realms/sahamati/clients"
        # validate 201 response code
        # call admin/realms/sahamati/clients
        # fetch the client_id and secret and return



    def get_public_key(self):
        """Gets the public key from Keycloak.

        Args:
          realm: The realm name.

        Returns:
          The public key as a PEM encoded string.
        """

        url = f"{self.conf['keycloak_base_url']}/realms/{self.conf['realm']}/protocol/openid-connect/certs"
        response = requests.get(url)
        print(response.text)
        if response.status_code != 200:
            raise ValueError("Failed to get public key from Keycloak")

        return response.text

    def validate_token(self, client_id, token):
        """Validates a Keycloak access token.

        Args:
          token: The access token to be validated.
          realm: The realm name.
          client_id: The client ID.

        Returns:
          True if the token is valid, False otherwise.
        """

        # Get the public key from Keycloak.
        public_key = self.get_public_key()
        print("public_key:::", public_key)

        # Decode the token.
        claims = jwt.decode(token, public_key, algorithms=["RS256"])
        print("Token:::::", token)
        # Use pycryptodome to decode the token.
        # claims = pycryptodome.jwt.decode(token, public_key, algorithms=["RS256"], verify_exp=True, verify_aud=True)

        # Check if the token is expired.
        if claims["exp"] < time.time():
            return False

        # Check if the token is valid for the specified client ID.
        if claims["client_id"] != client_id:
            return False

        return True
