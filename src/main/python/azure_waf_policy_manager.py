from azure.identity import DefaultAzureCredential
from azure.mgmt.network import NetworkManagementClient
from src.main.python.utils import azure_cred as az
import os
import json

from src.unittest.python.utils import read_config_file


class WAFPolicy:
    def __init__(self, client: NetworkManagementClient, resource_group_name: str, policy_name: str):
        self.client = client
        self.resource_group_name = resource_group_name
        self.policy_name = policy_name

    def get_custom_rules(self):
        response = self.client.web_application_firewall_policies.list(
            resource_group_name=self.resource_group_name,
        )
        existing_custom_rules = []
        for item in response:
            if item.custom_rules:
                existing_custom_rules.extend(item.custom_rules)
        return existing_custom_rules

    def add_custom_rules(self, new_custom_rules):
        all_custom_rules = self.get_custom_rules() + new_custom_rules
        response = self.client.web_application_firewall_policies.create_or_update(
            resource_group_name=self.resource_group_name,
            policy_name=self.policy_name,
            parameters={
                "location": "eastus",
                "properties": {
                    "customRules": all_custom_rules,
                    "managedRules": {
                        "managedRuleSets": [
                            {
                                "ruleSetType": "OWASP",
                                "ruleSetVersion": "3.2",
                                "ruleGroupOverrides": []
                            }
                        ],
                        "exclusions": []
                    }
                }
            }
        )
        return response


def configure_waf_policy():
    client = NetworkManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id=az.subscription_id
    )
    waf_policy = WAFPolicy(client, az.resource_group_name, az.waf_policy_name)

    read_azure_custom_rules = read_config_file.read_config(
        os.path.join(os.path.dirname(os.path.dirname(__file__)), "resources", "azure_custom_rules.json"))

    print(read_azure_custom_rules)
    new_custom_rules = [
        {
            "name": read_azure_custom_rules.get("ruleSetVersion"),
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
                    "negationConditon": False,
                    "matchValues": [
                        "192.168.3.0/24"
                    ],
                    "transforms": []
                }
            ]
        }
    ]

    response = waf_policy.add_custom_rules(new_custom_rules)
    return response

# # Define your dynamic values as variables
# location = "eastus"
#
# new_custom_rules = [
#     {
#         "name": "myrule4",
#         "priority": 1,
#         "ruleType": "MatchRule",
#         "action": "Allow",
#         "state": "Enabled",
#         "matchConditions": [
#             {
#                 "matchVariables": [
#                     {
#                         "variableName": "RemoteAddr"
#                     }
#                 ],
#                 "operator": "IPMatch",
#                 "negationConditon": False,
#                 "matchValues": [
#                     "192.168.3.0/24"
#                 ],
#                 "transforms": []
#             }
#         ]
#     }
# ]
#
# managed_rule_set = {
#     "ruleSetType": "OWASP",
#     "ruleSetVersion": "3.2",
#     "ruleGroupOverrides": []
# }
#
# def configure_waf_policy():
#     client = NetworkManagementClient(
#         credential=DefaultAzureCredential(),
#         subscription_id=az.subscription_id
#     )
#     waf_policy = WAFPolicy(client, az.resource_group_name, az.waf_policy_name)
#
#     response = waf_policy.add_custom_rules(new_custom_rules)
#     return response

if __name__ == "__main__":
    response = configure_waf_policy()
    print(response)













# from azure.identity import DefaultAzureCredential
# from azure.mgmt.network import NetworkManagementClient
# from src.main.python.utils import azure_cred as az
#
#
# class WAFPolicy:
#     def __init__(self, client: NetworkManagementClient, resource_group_name: str, policy_name: str):
#         self.client = client
#         self.resource_group_name = resource_group_name
#         self.policy_name = policy_name
#         self.location = "eastus"
#         self.custom_rules = []
#         self.managed_rules = {
#             "managedRuleSets": [
#                 {
#                     "ruleSetType": "OWASP",
#                     "ruleSetVersion": "3.2",
#                     "ruleGroupOverrides": []
#                 }
#             ],
#             "exclusions": []
#         }
#
#     def get_custom_rules(self):
#         response = self.client.web_application_firewall_policies.list(
#             resource_group_name=self.resource_group_name,
#         )
#         existing_custom_rules = []
#         for item in response:
#             if item.custom_rules:
#                 existing_custom_rules.extend(item.custom_rules)
#         return existing_custom_rules
#
#     def add_custom_rules(self, new_custom_rules):
#         all_custom_rules = self.get_custom_rules() + new_custom_rules
#         response = self.client.web_application_firewall_policies.create_or_update(
#             resource_group_name=self.resource_group_name,
#             policy_name=self.policy_name,
#             parameters={
#                 "location": self.location,
#                 "properties": {
#                     "customRules": all_custom_rules,
#                     "managedRules": self.managed_rules
#                 }
#             }
#         )
#         return response
#
#
#
#
#
# #
# #
# # class WAFPolicy:
# #     def __init__(self, client: NetworkManagementClient, resource_group_name: str, policy_name: str):
# #         self.client = client
# #         self.resource_group_name = resource_group_name
# #         self.policy_name = policy_name
# #
# #     def get_custom_rules(self):
# #         response = self.client.web_application_firewall_policies.list(
# #             resource_group_name=self.resource_group_name,
# #         )
# #         existing_custom_rules = []
# #         for item in response:
# #             if item.custom_rules:
# #                 existing_custom_rules.extend(item.custom_rules)
# #         return existing_custom_rules
# #
# #     # def add_custom_rules(self, new_custom_rules):
# #     #     all_custom_rules = self.get_custom_rules() + new_custom_rules
# #     #     response = self.client.web_application_firewall_policies.create_or_update(
# #     #         resource_group_name=self.resource_group_name,
# #     #         policy_name=self.policy_name,
# #     #         parameters={
# #     #             "location": location,
# #     #             "properties": {
# #     #                 "customRules": all_custom_rules,
# #     #                 "managedRules": {
# #     #                     "managedRuleSets": [
# #     #                         {
# #     #                             "ruleSetType": ruleSetType,
# #     #                             "ruleSetVersion": ruleSetVersion,
# #     #                             "ruleGroupOverrides": []
# #     #                         }
# #     #                     ],
# #     #                     "exclusions": []
# #     #                 }
# #     #             }
# #     #         }
# #     #     )
# #     #     return response
# #
# #     def add_custom_rules(self, new_custom_rules):
# #         all_custom_rules = self.get_custom_rules() + new_custom_rules
# #         config = {
# #             "location": "eastus",
# #             "customRules": all_custom_rules,
# #             "managedRules": {
# #                 "managedRuleSets": [
# #                     {
# #                         "ruleSetType": "OWASP",
# #                         "ruleSetVersion": "3.2",
# #                         "ruleGroupOverrides": []
# #                     }
# #                 ],
# #                 "exclusions": []
# #             }
# #         }
# #         response = self.client.web_application_firewall_policies.create_or_update(
# #             resource_group_name=self.resource_group_name,
# #             policy_name=self.policy_name,
# #             parameters={
# #                 "location": config["location"],
# #                 "properties": {
# #                     "customRules": config["customRules"],
# #                     "managedRules": config["managedRules"]
# #                 }
# #             }
# #         )
# #         return response
#
#
# def configure_waf_policy():
#     client = NetworkManagementClient(
#         credential=DefaultAzureCredential(),
#         subscription_id=az.subscription_id
#     )
#     waf_policy = WAFPolicy(client, az.resource_group_name, az.waf_policy_name)
#     new_custom_rules = [
#         {
#             "name": "myrule4",
#             "priority": 1,
#             "ruleType": "MatchRule",
#             "action": "Allow",
#             "state": "Enabled",
#             "matchConditions": [
#                 {
#                     "matchVariables": [
#                         {
#                             "variableName": "RemoteAddr"
#                         }
#                     ],
#                     "operator": "IPMatch",
#                     "negationConditon": False,
#                     "matchValues": [
#                         "192.168.3.0/24"
#                     ],
#                     "transforms": []
#                 }
#             ]
#         }
#     ]
#
#     response = waf_policy.add_custom_rules(new_custom_rules)
#     return response
#
#
# if __name__ == "__main__":
#     response = configure_waf_policy()
#     print(response)
