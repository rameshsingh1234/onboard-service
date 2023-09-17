import os

import pytest

from utilities.reusable import Reusable
from utilities.ExcelUtils import Excel
from utilities.ReadProperties import ReadConfig
from utilities.CustomLogger import LogGen


class TestApi:
    logger = LogGen.setup_logger(__name__,
                                 os.path.join(os.path.dirname(os.path.abspath(__file__)), '../logs/automation.log'))

    @pytest.mark.parametrize(
        "scenario_id,scenario,scenario_description,api_method,api_endpoint,payload,expected_status_code,"
        "response_status_name,expected_api_response,actual_api_response,result",
        Excel.get_data())
    def test_access(self, scenario_id, scenario, scenario_description, api_method, api_endpoint, payload,
                    expected_status_code, response_status_name, expected_api_response, actual_api_response, result):
        self.logger.info("**********"+scenario_id+"is started **********")
        self.logger.info("**********"+scenario_description+"**********")
        endpoint = ReadConfig.get_api_url() + api_endpoint
        headers = {
            'Content-Type': 'application/json'
        }
        response = Reusable.call_requests(api_method, endpoint, headers, payload)
        assert int(expected_status_code) == response.status_code
        self.logger.info("**********" + scenario_id + "is ended **********")
