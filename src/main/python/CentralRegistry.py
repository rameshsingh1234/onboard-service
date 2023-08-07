import json

import requests
from src.unittest.python.utils import read_config_file


class CentralRegistry:
    def __init__(self,config, entity_type):
        self.config = config
        self.entity_type = entity_type

    def get_entity_by_id(self, entity_id):
        """
        call the get  entity api
        :return the JSON response with the status code
        """
        # config = read_config_file.read_config('/home/krishna/Tibil/sahamati/onboard-service/src/main/python/resources'
        #                                       '/application.json')

        url = f"{self.config.get('central_registry_url')}/entityInfo/{self.entity_type}/{entity_id}"

        payload = ""
        headers = {}

        response = requests.request("GET", url)
        return response

    def add_entity(self, entity_info):
        """
        call the post save entity api
        :return the JSON response with the status code
        """
        access_token ='eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJ3N2RmZkhZS0JvUzJJUTFhU0t1YjZTcUtRUUI4d2NTWkFzTEpfN19IWXg0In0.eyJleHAiOjE2OTE0NDMxMDgsImlhdCI6MTY5MTQwNzEwOCwianRpIjoiNjNkOTIyZDQtYzVjYi00NTM2LWJjYzItN2E2MGE5NzBhMTJlIiwiaXNzIjoiaHR0cDovL2xvY2FsaG9zdDo4MDgwL3JlYWxtcy9zYWhhbWF0aSIsImF1ZCI6WyJyZWFsbS1tYW5hZ2VtZW50IiwiYWNjb3VudCJdLCJzdWIiOiIxYjk1ODdjOC1kY2ZhLTQxZjAtYmZlYy1mMDUxNDcwMTRjMDkiLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJzYWhhbWF0aS1hZG1pbiIsImFjciI6IjEiLCJhbGxvd2VkLW9yaWdpbnMiOlsiLyoiXSwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbImRlZmF1bHQtcm9sZXMtc2FoYW1hdGkiLCJvZmZsaW5lX2FjY2VzcyIsInVtYV9hdXRob3JpemF0aW9uIl19LCJyZXNvdXJjZV9hY2Nlc3MiOnsic2FoYW1hdGktYWRtaW4iOnsicm9sZXMiOlsidW1hX3Byb3RlY3Rpb24iXX0sInJlYWxtLW1hbmFnZW1lbnQiOnsicm9sZXMiOlsibWFuYWdlLXVzZXJzIl19LCJhY2NvdW50Ijp7InJvbGVzIjpbIm1hbmFnZS1hY2NvdW50IiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJ2aWV3LXByb2ZpbGUiXX19LCJzY29wZSI6InByb2ZpbGUgZW1haWwiLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsImNsaWVudEhvc3QiOiIxNzIuMTcuMC4xIiwicHJlZmVycmVkX3VzZXJuYW1lIjoic2VydmljZS1hY2NvdW50LXNhaGFtYXRpLWFkbWluIiwiY2xpZW50QWRkcmVzcyI6IjE3Mi4xNy4wLjEiLCJjbGllbnRfaWQiOiJzYWhhbWF0aS1hZG1pbiJ9.Nbz4L8BxhYE279I3lMS9EdsBZaNFTaMTc7tt2sBQWEFq1QUU2gq2biRJMQC3vrAP3cudpbGEUn2-uH07a4wiAuoOi_UJI6YiXkJ_QO5Qb5eAe6o4MCH0NQZJjJL_uYr5woByb1Ry52BVwPFXYAUPVRm27xPs0B79uRXMuBZiQ6XGwQYRQNvjXgz3YKLPp96mopzit35nWDT-3oIo8nGZuE4gCtKVesLAI5bHK0j4FI68KMol7RD4sf8kPAQl4g8H0go9RrDoghmBte7sNMKU8NXvgDx8mk53zW5sFt8iGunViP2OZ0szapviXmh1V5mcsGUTmaz-ej12VTmfmZ4M8g'
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json'
        }

        url = f"{self.config.get('central_registry_url')}/entityInfo/{self.entity_type}"

        response = requests.request("POST", url, headers=headers, data=json.dumps(entity_info))
        print("add_entity_res::",response.text)
        return response

