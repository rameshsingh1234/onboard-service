import json
import requests


class CentralRegistry:
    """
    This class is responsible for Interacting with the Central Registry APIs.

    Methods:
    - add_entity(entity_info, access_token): Adds a new entity to the CR.
    - get_entity_by_id(entity_id): Returns the entity details from the CR.
    
    Usage:
    registry = CentralRegistry(config, entity_type)
    registry.add_entity(entity_info, access_token)
    registry.get_entity_by_id(entity_id)
    """

    def __init__(self, config, entity_type):
        self.config = config
        self.entity_type = entity_type

    def add_entity(self, entity_info, access_token):
        """
        Save entity information to a CR using a POST request
        :param entity_info: the entity information to be saved
        :param access_token: the access token for authentication
        :return: the JSON response with the status code
        """        
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json'
        }

        url = f"{self.config.get('central_registry_url')}/entityInfo/{self.entity_type}"
        response = requests.request("POST", url, headers=headers, data=json.dumps(entity_info))
        return response
    
    def get_entity_by_id(self, entity_id):
        """
        call the get  entity api
        :return the JSON response with the status code
        """

        url = f"{self.config.get('central_registry_url')}/entityInfo/{self.entity_type}/{entity_id}"

        response = requests.request("GET", url)
        return response

