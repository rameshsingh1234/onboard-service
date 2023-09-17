import requests


class Reusable:
    @staticmethod
    def call_requests(method,endpoint,headers,payload):
        try:
             response = requests.request(method, endpoint, headers=headers, data=payload)
             return response
        except requests.exceptions.HTTPError as e:
            print(e.response.text)

