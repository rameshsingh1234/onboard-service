# import os
# from azure.identity import DefaultAzureCredential
# from azure.mgmt.network import NetworkManagementClient
# from src.main.python.azure_waf_policy_manager import WAFPolicy, MatchVariable, CustomRule, MatchCondition, ManagedRuleSets
# from src.main.python.utils import azure_cred as az
# from src.unittest.python.utils import read_config_file
# import pytest
#
#
# @pytest.mark.parametrize("correct_ip", ["192.168.3.0/24", "10.0.0.0/16"])
# def test_validate_correct_ip_rule_added(correct_ip):
#     """
#     Load the configuration data from the JSON file
#     Create an instance of the Azure client
#     Create an instance of the WAFPolicy class
#     Prepare the new custom rules based on the configuration
#     Prepare an empty ManagedRuleSets object
#     Call the add_custom_rules method
#     Fetch the existing custom rules
#     Validate that the new custom rule with correct IP has been added
#
#     """
#     config_path = read_config_file.read_config(
#         os.path.join(os.path.dirname(os.path.dirname(__file__)), "../../main/python/resources",
#                      "azure_custom_rules.json"))
#     custom_rules_config = config_path["custom_rules"]
#
#     client = NetworkManagementClient(
#         credential=DefaultAzureCredential(),
#         subscription_id=az.subscription_id
#     )
#
#     waf_policy = WAFPolicy(client, az.resource_group_name, az.waf_policy_name)
#
#     new_custom_rules = []
#     for custom_rule_data in custom_rules_config:
#         match_variables = [MatchVariable(variable_name) for variable_name in custom_rule_data["match_variables"]]
#         match_condition = MatchCondition(
#             match_variables=match_variables,
#             operator=custom_rule_data["operator"],
#             negation_condition=custom_rule_data["negation_condition"],
#             match_values=custom_rule_data["match_values"],
#             transforms=custom_rule_data["transforms"]
#         )
#         new_custom_rule = CustomRule(
#             name=custom_rule_data["name"],
#             priority=custom_rule_data["priority"],
#             rule_type=custom_rule_data["rule_type"],
#             action=custom_rule_data["action"],
#             state=custom_rule_data["state"],
#             match_conditions=[match_condition]
#         )
#         new_custom_rules.append(new_custom_rule)
#
#     managed_rule_sets = ManagedRuleSets(rule_sets=[], exclusions=[])
#
#     waf_policy.add_custom_rules(new_custom_rules, managed_rule_sets)
#
#     existing_custom_rules = waf_policy.get_custom_rules()
#
#     correct_ip_added = any(
#         rule.match_conditions[0].match_values[0] == correct_ip
#         for rule in existing_custom_rules
#     )
#     assert correct_ip_added
