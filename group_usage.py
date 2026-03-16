from shadowtrackr import ShadowTrackr
from time import sleep
from pprint import pprint

# This example is only for multi-tenant accounts
# A groupcode allows you to automate management of separate organizations.

API_KEY = "CHANGEME"
GROUPCODE = "CHANGEME"

# initialize the group account and create a new organization in it
st_group = ShadowTrackr(api_key=API_KEY)
new_org = st_group.create_organization("My Test Org", GROUPCODE)
print("The new organization:")
pprint(new_org)

# initialize the new organization account, and add a url
st_new_org = ShadowTrackr(api_key=API_KEY)
st_new_org.add_assets("shadowtrackr.com")

sleep(600)

websites = st_new_org.websites()
print("Websites found for the new organization:")
pprint(websites)

sleep(3)
print("The list off currently active organizations in the group: ")
pprint(st_group.organizations(GROUPCODE, full=True))

# delete the new organization from the group
sleep(3)
result = st_group.delete_organization(new_org['organization_id'], GROUPCODE)
print("Result of deleting")
pprint(result)

