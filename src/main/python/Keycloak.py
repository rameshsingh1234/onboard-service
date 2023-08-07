#import necessary libraries

class Keycloak:
    def read_client_id(self):
        """
        Read the clientID from the Config file
        call the keycloak get client api
        return clientID (set of response)
        compare the both the client id's
        condition is true 200 ok response
        else specific messages with response code
        """

    def get_token(self):
        """
        call the keycloak post method api
        in header pass clientId and secrete
        hit the api to get the access token
        """

    def create_client(self):
        """
        call the post method create client keycloak api
        header: application/json
        Authorization: AccessToken
        request body:
        :return:
        """