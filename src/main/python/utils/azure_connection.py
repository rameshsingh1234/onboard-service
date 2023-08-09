# Python code to connect with azure account

from azure.identity import DefaultAzureCredential
from azure.mgmt.web import WebSiteManagementClient


def add_cidr_to_waf():
    # Initialize Azure credentials
    credentials = DefaultAzureCredential()

    # Initialize Azure WAF client
    subscription_id = "<subscription_id>"
    resource_group_name = "<resource_group_name>"
    waf_policy_name = "<waf_policy_name>"

    waf_client = WebSiteManagementClient(credentials, subscription_id)

    try:
        # Retrieve existing WAF policy
        waf_policy = waf_client.web_application_firewall_policies.get(resource_group_name, waf_policy_name)

        # Add CIDR range to the custom rules
        custom_rule = {
            "name": "CustomRule1",
            "rule_type": "MatchRule",
            "action": "Allow",
            "match_conditions": [{
                "match_variables": [{
                    "variable_name": "RemoteAddr",
                    "selector": "RemoteAddr",
                    "operator": "IPMatch",
                    "negation_condition": False,
                    "match_values": ["<your_cidr_range>"]
                }]
            }]
        }

        # Add the custom rule to the policy
        waf_policy.custom_rules.append(custom_rule)

        # Update WAF policy
        waf_client.web_application_firewall_policies.create_or_update(resource_group_name, waf_policy_name, waf_policy)

        print("CIDR range added to Azure WAF successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    add_cidr_to_waf()
