import os

import pytest

from test.utilities.reusable import Reusable
from test.utilities.ExcelUtils import Excel
from test.utilities.ReadProperties import ReadConfig
from test.utilities.CustomLogger import LogGen


class TestApi:
    logger = LogGen.setup_logger(__name__,
                                 os.path.join(os.path.dirname(os.path.abspath(__file__)), '../logs/automation.log'))

    @pytest.mark.parametrize(
        "scenario_id,scenario,scenario_description,api_method,api_endpoint,payload,expected_status_code,"
        "response_status_name,expected_api_response,actual_api_response,result",
        Excel.fiu_get_data())
    def test_access(self, scenario_id, scenario, scenario_description, api_method, api_endpoint, payload,
                    expected_status_code, response_status_name, expected_api_response, actual_api_response, result):
        self.logger.info("**********"+scenario_id+"is started **********")
        self.logger.info("**********"+scenario_description+"**********")
        endpoint = ReadConfig.get_api_url() + api_endpoint
        # headers = {
        #     'clientId': 'sahamati-admin',
        #     'clientSecret': 'Eqt2Q8L5mc2QsfcVv147fvDyxxQP4SMN',
        #     'userType': 'sahamati-ops',
        #     'Content-Type': 'application/json',
        #     'Accept': 'application/json'
        # }
        print("....",scenario_id)
        if scenario_id == "Tc_sahamati_Onborading_FIU_001":
            print(1)
        elif scenario_id == "Tc_sahamati_Onborading_FIU_002":
            print(2)
        elif scenario_id == "Tc_sahamati_Onborading_FIU_003":
            print(3)
        elif scenario_id == "Tc_sahamati_Onborading_FIU_004":
            print(4)

        #
        # response = Reusable.call_requests(api_method, endpoint, headers, payload)
        # assert int(expected_status_code) == response.status_code
        # self.logger.info("**********" + scenario_id + "is ended **********")











    # @pytest.mark.parametrize(
    #     "scenario_id,scenario,scenario_description,api_method,api_endpoint,payload,expected_status_code,"
    #     "response_status_name,expected_api_response,actual_api_response,result",
    #     Excel.fiu_get_data())
    # def test_access(self, scenario_id, scenario, scenario_description, api_method, api_endpoint, payload,
    #                 expected_status_code, response_status_name, expected_api_response, actual_api_response, result):
    #     self.logger.info("**********" + scenario_002 + " is started **********")
    #     self.logger.info("**********" + Verify_to_create_new_entity_without_giving_access_token + " **********")
    #     endpoint = ReadConfig.get_api_url() + api_endpoint
    #     headers = {
    #         'Content-Type': 'application/json',
    #         'Accept': 'application/json',
    #     }
    #     response = Reusable.call_requests(api_method, endpoint, headers, payload)
    #     if int(expected_status_code) == 401:
    #         assert response.status_code == 401
    #     else:
    #         assert int(expected_status_code) == response.status_code
    #
    #     self.logger.info("**********" + scenario_id + " is ended **********")
    #
    #
