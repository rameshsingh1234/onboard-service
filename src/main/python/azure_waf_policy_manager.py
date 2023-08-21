from azure.identity import DefaultAzureCredential
from azure.mgmt.network import NetworkManagementClient
from src.main.python.utils import azure_cred as az


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
            print(item)
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
        print(response)


# if __name__ == "__main__":
#
#     client = NetworkManagementClient(
#         credential=DefaultAzureCredential(),
#         subscription_id=az.subscription_id
#     )
#     waf_policy = WAFPolicy(client, az.resource_group_name,az.waf_policy_name)
#     new_custom_rules = [{
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
#     }]
#     waf_policy.add_custom_rules(new_custom_rules)
