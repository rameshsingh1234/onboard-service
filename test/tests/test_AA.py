import configparser
import csv
import os
import os

import json
import pytest

from test.utilities.reusable import Reusable
from test.utilities.ExcelUtils import Excel
from test.utilities.ReadProperties import ReadConfig, config
from test.utilities.CustomLogger import LogGen
from test.utilities import reusable


def get_data():
    configuartion_path = os.path.dirname(os.path.abspath(__file__))
    parent_folder = os.path.dirname(configuartion_path) + '/resources/configurations/config.ini'
    config = configparser.ConfigParser()
    config.read(parent_folder)

    with open(config['CREDs']['csv'], 'r') as f:
        reader = csv.reader(f)
        next(reader)
        data = [list(row) for row in reader]
    return data


@pytest.mark.parametrize(
    "scenario_id,scenario,test_case_description,api_method,api_endpoint,payload,expected_status_code,"
    "response_status_name,expected_api_response,actual_api_response,result,userType,Content_Type,Accept",
    Excel.get_data())
def test_access(scenario_id, scenario, test_case_description, api_method, api_endpoint, payload,
                expected_status_code, response_status_name, expected_api_response, actual_api_response, result,
                userType, Content_Type, Accept):
    credentials = Excel.read_client_credentials(Excel.csv_file)
    print("payload**********", payload)
    endpoint = ReadConfig.get_api_url2() + api_endpoint
    headers = {
        'clientId': credentials[0]['clientId'],
        'clientSecret': credentials[0]['clientSecret'],
        'userType': userType,
        'Content-Type': Content_Type,
        'Accept': Accept,
    }
    payload_dict = json.loads(payload)
    print("payloadd************", payload_dict)
    print("before adding new id:test_AA:", payload_dict)
    print("current requester id , from test data", payload_dict['requester']['id'])
    test_id = reusable.read_csv_entity()
    print("test_id*******************", test_id)
    payload_dict['requester']['id'] = test_id
    payload_dict['entityinfo']['id'] = test_id
    print("payload_dict", payload_dict)
    # # payload_dict['certificate']['kid'] = test_id
    print("after adding new id:test_AA:", payload_dict)
    updated_payload = json.dumps(payload_dict)
    response = Reusable.call_requests(api_method, endpoint, headers, updated_payload)
    print("Response Status Code################", response.status_code)
    assert int(expected_status_code) == response.status_code















# class TestApi:
#     logger = LogGen.setup_logger(__name__,
#                                  os.path.join(os.path.dirname(os.path.abspath(__file__)), '../logs/automation.log'))
#
#     @pytest.mark.parametrize(
#         "scenario_id,scenario,test_case_description,api_method,api_endpoint,payload,expected_status_code,"
#         "response_status_name,expected_api_response,actual_api_response,result",
#         Excel.get_data())
#     def test_access(self, scenario_id, scenario,test_case_description, api_method, api_endpoint, payload,
#                     expected_status_code, response_status_name, expected_api_response, actual_api_response, result):
#         self.logger.info("************Test_001**************")
# #         self.logger.info("************Verifying create new entity with")
#         endpoint = ReadConfig.get_api_url() + api_endpoint
#         headers = {
#             'clientId': config.get('Credentials', 'clientId'),
#             'clientSecret': config.get('Credentials', 'clientSecret'),
#             'userType': config.get('Credentials', 'userType'),
#             'Content-Type': config.get('Headers', 'Content-Type'),
#             'Accept': config.get('Headers', 'Accept')
#         }
#         if scenario_id == "Tc_sahamati_Onborading_AA_001":
#             payload_dict = json.loads(payload)
#             id = Reusable.get_id("/entityInfo/AA")
#             print(id)
#             payload_dict['requester']['id'] = id
#             updated_payload = json.dumps(payload_dict)
#             print(updated_payload)
# #
#             response = Reusable.call_requests(api_method, endpoint, headers, payload)
#             print("Response Status Code:", response.status_code)
#             assert int(expected_status_code) == response.status_code
#             self.logger.info("**********" + scenario_id + "is ended **********")
#         elif scenario == "Tc_sahamati_Onborading_AA_001":
#             response = Reusable.call_requests(api_method, endpoint, headers, payload)
#             assert int(expected_status_code) == response.status_code


# Read the test data file
# data = get_data()
#
# for i in data:
#     print("TEST case id:=", i[0])
#     if i[0].startswith('Tc_sahamati_Onborading_AA'):
#         print("inside if TEST case id:=", i[0])
#         api_endpoint = i[4]
#         payload = i[5]
#         api_method = i[3]
#         print(api_method)
#         expected_status_code = i[6]
#         userType = i[11]
#         Content_Type = i[12]
#         Accept = i[13]
#         endpoint = ReadConfig.get_api_url2() + api_endpoint
#         print(endpoint)
#         headers = {
#             'clientId': config['Credentials']['clientId'],
#             'clientSecret': config['Credentials']['clientSecret'],
#             'userType': userType,
#             'Content-Type': Content_Type,
#             'Accept': Accept,
#         }
#         payload_dict = json.loads(payload)
#         # id = Reusable.get_id("/entityInfo/AA")
#         # print("Existing entity ID:",id, len(id))
#         # if len(id) > 0:
#
#         # print("random id generation check",read_csv_entity())
#
#         # if id != 0:
#         print("before adding new id:test_AA:", payload_dict)
#         # print("new entity id:: ",read_csv_entity())
#         print("current requester id , from test data", payload_dict['requester']['id'])
#         test_id = reusable.read_csv_entity()
#         payload_dict['requester']['id'] = test_id
#         payload_dict['entityinfo']['id'] = test_id
#         #       payload_dict['certificate']['kid'] = test_id
#
#         print("after adding new id:test_AA:", payload_dict)
#         updated_payload = json.dumps(payload_dict)
#         # print("updated_payload:test_AA:",payload_dict)
#         # response = Reusable.call_requests(api_method, endpoint, headers, payload_dict)
#         response = Reusable.call_requests(api_method, endpoint, headers, updated_payload)
#         print("Response Status Code################", response.status_code)
#         assert int(expected_status_code) == response.status_code
