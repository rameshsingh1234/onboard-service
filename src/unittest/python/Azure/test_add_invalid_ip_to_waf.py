import pytest
from azure.identity import DefaultAzureCredential
from azure.mgmt.network import NetworkManagementClient
from src.main.python.azure_waf_policy_manager import WAFPolicy
from src.main.python.utils import azure_cred as az


@pytest.mark.parametrize("incorrect_ip", ["10.0.0.1", "192.168.1.0/24", "invalid_ip"])
def test_add_incorrect_ip_rule_to_waf(incorrect_ip):
    # Set your Azure subscription and resource details here
    subscription_id = az.subscription_id
    resource_group_name = az.resource_group_name
    waf_policy_name = az.waf_policy_name

    # Create an instance of the Azure client
    client = NetworkManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id=subscription_id
    )

    # Create an instance of the WAFPolicy class
    waf_policy = WAFPolicy(client, resource_group_name, waf_policy_name)

    # Define the new custom rule with incorrect IP
    new_custom_rules = [
        {
            "name": "myrule_invalid_ip",
            "priority": 1,
            "ruleType": "MatchRule",
            "action": "Allow",
            "state": "Enabled",
            "matchConditions": [
                {
                    "matchVariables": [
                        {
                            "variableName": "RemoteAddr"
                        }
                    ],
                    "operator": "IPMatch",
                    "negationCondition": False,
                    "matchValues": [
                        incorrect_ip
                    ],
                    "transforms": []
                }
            ]
        }
    ]

    # Call the add_custom_rules method
    waf_policy.add_custom_rules(new_custom_rules)

    # Fetch the existing custom rules
    existing_custom_rules = waf_policy.get_custom_rules()

    # Validate that the new custom rule with incorrect IP has not been added
    assert not any(
        rule["matchConditions"][0]["matchValues"][0] == incorrect_ip
        for rule in existing_custom_rules
    )
