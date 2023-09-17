# import os
# from azure.identity import DefaultAzureCredential
# from azure.mgmt.network import NetworkManagementClient
# from src.main.python.utils import azure_cred as az
# from src.unittest.python.utils import read_config_file
#
# config_path = read_config_file.read_config(
#     os.path.join(os.path.dirname(os.path.dirname(__file__)), "../main/python/resources", "azure_custom_rules.json"))
#
#
# class RuleSet:
#     def __init__(self, rule_set_type, rule_set_version, rule_group_overrides=None):
#         self.ruleSetType = rule_set_type
#         self.ruleSetVersion = rule_set_version
#         self.ruleGroupOverrides = rule_group_overrides or []
#
#
# class ManagedRuleSets:
#     def __init__(self, rule_sets, exclusions=None):
#         self.managedRuleSets = rule_sets
#         self.exclusions = exclusions or []
#
#
# class Properties:
#     def __init__(self, custom_rules, managed_rules):
#         self.customRules = custom_rules
#         self.managedRules = managed_rules
#
#
# class PolicyParameters:
#     def __init__(self, location, properties):
#         self.location = location
#         self.properties = properties
#
#
# class MatchVariable:
#     def __init__(self, variable_name):
#         self.variableName = variable_name
#
#
# class MatchCondition:
#     def __init__(self, match_variables, operator, negation_condition, match_values, transforms):
#         self.matchVariables = match_variables
#         self.operator = operator
#         self.negationConditon = negation_condition
#         self.matchValues = match_values
#         self.transforms = transforms
#
#
# class CustomRule:
#     def __init__(self, name, priority, rule_type, action, state, match_conditions):
#         self.name = name
#         self.priority = priority
#         self.ruleType = rule_type
#         self.action = action
#         self.state = state
#         self.matchConditions = match_conditions
#
#
# class WAFPolicy:
#     def __init__(self, client: NetworkManagementClient, resource_group_name: str, policy_name: str):
#         self.client = client
#         self.resource_group_name = resource_group_name
#         self.policy_name = policy_name
#
#     def get_custom_rules(self):
#         response = self.client.web_application_firewall_policies.list(
#             resource_group_name=self.resource_group_name,
#         )
#         existing_custom_rules = []
#         for item in response:
#             print(item)
#             if item.custom_rules:
#                 existing_custom_rules.extend(item.custom_rules)
#         return existing_custom_rules
#
#     def add_custom_rules(self, new_custom_rules, managed_rule_sets):
#         all_custom_rules = self.get_custom_rules() + new_custom_rules
#
#         properties = Properties(all_custom_rules, managed_rule_sets)
#         policy_params = PolicyParameters(config_path["location"], properties)
#         print(policy_params)
#
#         response = self.client.web_application_firewall_policies.create_or_update(
#             resource_group_name=self.resource_group_name,
#             policy_name=self.policy_name,
#             parameters=policy_params
#         )
#         print(response)
#
#
# def configure_waf_policy():
#     client = NetworkManagementClient(
#         credential=DefaultAzureCredential(),
#         subscription_id=az.subscription_id
#     )
#     waf_policy = WAFPolicy(client, az.resource_group_name, az.waf_policy_name)
#
#     new_custom_rules = []
#     for custom_rule_data in config_path["custom_rules"]:
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
#     waf_policy.add_custom_rules(new_custom_rules, managed_rule_sets)
