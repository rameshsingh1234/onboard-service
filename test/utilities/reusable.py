# import json
# import random
import csv
import uuid
from test.utilities.ReadProperties import ReadConfig

# #
# import requests
#
# from test.utilities.ReadProperties import ReadConfig
#
#
# class Reusable:
# @staticmethod
# def call_requests(method,endpoint,headers,payload):
#     try:
#          response = requests.request(method, endpoint, headers=headers, data=payload)
#          return response
#     except requests.exceptions.HTTPError as e:
#         print(e.response.text)
#
# @staticmethod
# def get_id(end_point):
#     headers = {
#         'clientId': 'sahamati-admin',
#         'clientSecret': 'Eqt2Q8L5mc2QsfcVv147fvDyxxQP4SMN',
#     'userType': 'sahamati-ops',
#     'Content-Type': 'application/json',
#     'Accept': 'application/json'
# }
# endpoint = ReadConfig.get_api_url() + end_point
# response = Reusable.call_requests("get", endpoint, headers, "")
# output = json.loads(response.text)
# lst = []
# for x in output:
#     res = x.get("entityinfo")
#     lst.append(res.get("id"))
#
# id = 0
# while True:
#     temp = random.randint(0, 1000000)
#     if temp != lst:
#         id = temp
#         break
# return id

#
# import uuid

#
# def generate_new_id():
#     return str(uuid.uuid4())
#
# lst = ["fiu2@finarkein","fiu3@finarkein", "fiu@finarkein", "fiu1@finarkein"]
# url = "http://localhost:9595/entityInfo/FIU"
# response = requests.get(url)
# if response.status_code == 200:
#     data = response.json()
#     lst = []
#
#     for item in data:
#         entity_id = item.get("entityinfo").get("id")
#         if entity_id in lst:
#             new_id = generate_new_id()
#             lst.append({"entityinfo": {"id": new_id}})
#         else:
#             lst.append({"entityinfo": {"id": entity_id}})
#
#     print("Updated Data:", lst)
# else:
#     print("Failed to retrieve data. Status code:", response.status_code)


#
#
#
# def generate_new_id():
#     return str(uuid.uuid4())
#
#
# import csv
# import json
# import uuid
#
# import requests
# # from test.utilities.ReadProperties import ReadConfig
#
#
# class Reusable:
#     @staticmethod
#
#     def call_requests(method, endpoint, headers, payload):
#         # reusable_instance = Reusable()
#         # cr_entity_ids = reusable_instance.get_id("http://localhost:9595/entityInfo/AA")
#         try:
#             response = requests.request(method, endpoint, headers=headers, data=payload)
#             return response
#         except requests.exceptions.HTTPError as e:
#             print(e.response.text)
#
#     @staticmethod
#     def get_id(end_point):
#         headers = {
#             'clientId': 'sahamati-admin',
#             'clientSecret': 'Eqt2Q8L5mc2QsfcVv147fvDyxxQP4SMN',
#             'userType': 'sahamati-ops',
#             'Content-Type': 'application/json',
#             'Accept': 'application/json'
#         }
#         # endpoint = ReadConfig.get_api_url() + end_point
#         base_url = ReadConfig.get_api_url()
#         end_point = '/entityInfo/AA'
#         endpoint = base_url + end_point
#         # reusable_instance = Reusable()
#         # # cr_entity_ids = reusable_instance.get_id("http://localhost:9595/entityInfo/AA")
#
#         response =  Reusable.call_requests("get", endpoint, headers, "")
#         output = json.loads(response.text)
#         lst = []
#         for x in output:
#             # res = x.get("entityinfo")
#             # lst.append(res.get("id")
#             print(x)
#
#         return lst
#     get_id("http://localhost:9595")
#
#
#
# def read_csv_entity():
#     cr_entity_ids = Reusable.get_id("http://localhost:9595/entityInfo/AA")
#
#     test_data_entity_ids = []
#     with open(
#             '/home/tanushree/Documents/vishAAs-Onboar_service/onboard-service/test/resources/test_data/Onboarding_API - '
#             'AA.csv', 'r') as csv_file:
#         csv_reader = csv.DictReader(csv_file)
#         for row in csv_reader:
#             payload = row['PayLoad']
#             payload_dict = json.loads(payload)
#             requester_info = payload_dict.get('requester', {})
#             aatest_entity = requester_info.get('id')
#             if aatest_entity is not None:
#                 test_data_entity_ids.append(aatest_entity)
#                 print(f'AAtestEntity: {aatest_entity}')
#
#     if cr_entity_ids == test_data_entity_ids:
#         new_entity_id = str(uuid.uuid4())
#         print(f"Create new entity ID: {new_entity_id}")
#     else:
#         same_entity_id = cr_entity_ids[0]
#         print(f"Pass the same entity ID: {same_entity_id}")
#
# # if set(cr_entity_ids) == set(test_data_entity_ids):


import csv
import json
import uuid
import requests
from test.utilities.ReadProperties import ReadConfig


class Reusable:
    @staticmethod
    def call_requests(method, endpoint, headers, payload):
        print('inside call requests payload:resuable:: ', payload)

        try:
            response = requests.request(method, endpoint, headers=headers, data=payload)
            print("Reusable#########################", method)
            return response
        except requests.exceptions.HTTPError as e:
            print(e.response.text)

    @staticmethod
    def get_id(end_point):
        headers = {
            'clientId': 'sahamati-admin',
            'clientSecret': 'Eqt2Q8L5mc2QsfcVv147fvDyxxQP4SMN',
            'userType': 'sahamati-ops',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        base_url = ReadConfig.get_api_url()
        endpoint = base_url + end_point
        print(endpoint)
        response = Reusable.call_requests("get", endpoint, headers, "")
        output = json.loads(response.text)
        lst = []
        # if output.get("expected_status_code") == 201:
        #     for x in output:
        #         res = x.get("entityinfo")
        #         lst.append(res.get("id"))
        #     return lst
        # else :
        #     return lst
        # print(response.status_code, response.text)
        if response.status_code == 200:
            output = json.loads(response.text)
            lst_entity_ids = []
            list_kid = []
            # print(lst)
            for x in output:
                res = x.get("entityinfo")
                print(res)
                lst_entity_ids.append(res.get("id"))
                list_kid.append(res.get("certificate").get("kid"))

            return lst_entity_ids,list_kid
        else:
            return []


def read_csv_entity():
    reusable_instance = Reusable()
    cr_entity_ids = reusable_instance.get_id("/entityInfo/AA")

    test_data_entity_ids = []
    test_kid_id = []
    # print("re__________________",test_data_entity_ids)
    with open(
            '/home/ramesh/onboard-service/test/resources/test_data/Onboarding_API - AA.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            payload = row['payload']
            payload_dict = json.loads(payload)
            requester_info = payload_dict.get('requester', {})
            aatest_entity = requester_info.get('id')
            if aatest_entity is not None:
                test_data_entity_ids.append(aatest_entity)
                print(f'AAtestEntity: {aatest_entity}')

    if set(cr_entity_ids) == set(test_data_entity_ids):
        new_entity_id = str(uuid.uuid4())
        print(new_entity_id)
        # kid_id = str(uuid.uuid4())
        # print(f"Create new entity ID: {kid_id}")
        print(f"Create new entity ID: {new_entity_id}")
        return new_entity_id

    else:
        same_entity_id = test_data_entity_ids[0]
        print(f"Pass the same entity ID: {same_entity_id}")
        return same_entity_id

