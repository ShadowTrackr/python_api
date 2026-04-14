from shadowtrackr import ShadowTrackr
from time import sleep
import json

# This example is only for multi-tenant accounts
# A groupcode allows you to automate management of separate organizations.

API_KEY = "CHANGEME"
GROUPCODE = "CHANGEME"

# initialize the group account and create a new organization in it
st_group = ShadowTrackr(api_key=API_KEY)

result = st_group.add_organization(name="My Test Org", groupcode=GROUPCODE)
print(json.dumps(result, indent=2))

if result['error']:
    exit(1)

print("The new organization:")
new_org = result['data']
print(json.dumps(new_org, indent=2))

# initialize the new organization account, and add a url

st_new_org = ShadowTrackr(api_key=new_org['api_key'])
result = st_new_org.add_assets("shadowtrackr.com")
print(json.dumps(result, indent=2))

sleep(600)

websites = st_new_org.websites()
print("Websites found for the new organization:")
print(json.dumps(websites, indent=2))

sleep(3)
print("The list off currently active organizations in the group: ")
result = st_group.organizations(groupcode=GROUPCODE)
print(json.dumps(result, indent=2))

# delete the new organization from the group
sleep(3)
result = st_group.delete_organization(oid=new_org['oid'], groupcode=GROUPCODE)
print("Result of deleting")
print(json.dumps(result, indent=2))

