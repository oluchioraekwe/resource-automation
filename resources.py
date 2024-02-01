import os

from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient
from dotenv import load_dotenv

load_dotenv(".env")
credential = AzureCliCredential()


# subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]
subscription_id = os.environ["SUBSCRIPTION_ID"]


resource_client = ResourceManagementClient(credential, subscription_id)

# rg = resource_client.resource_groups.create_or_update(
#     "demo_rg",{"location":"uksouth"}
# )

# print(
#     f"Provisioned resource group {rg.name} in \
#     the {rg.location} region"
# )

# rg = resource_client.resource_groups.create_or_update(
#     "demo_rg",
#     {
#         "location":"uksouth",
#         "tags":{
#             "environment":"staging",
#             "department" : "IT"
#                }
#     }
# )

list_rg = resource_client.resource_groups.list()

# print(
#     f"Updated resource group {rg.name} in \
#     the {rg.location} region with tags"
# )
print("List of my resource groups")
for rg in list_rg:
    print("Id: {}".format(rg.id))
    print("Name: {}".format(rg.name))
# print(list_rg)
