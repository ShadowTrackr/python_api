from shadowtrackr import ShadowTrackr
from time import sleep

# This example is only for those who have a groupcode.
# A groupcode allows you to automate management of separate accounts.
# Only available in custom subscriptions, contact support@shadowtrackr.com

API_KEY = "YOUR_API_KEY"
GROUPCODE = "YOUR_GROUPCODE"

st = ShadowTrackr(api_key=API_KEY)

new_org = st.create_organization("My Test Org", GROUPCODE)
print(new_org)

sleep(3)
print("After creating: ")
print(st.get_active_organizations(GROUPCODE))

sleep(3)
result = st.delete_organization(new_org['organization_id'], GROUPCODE)
print(result)

sleep(3)
print("After deleting: ")
print(st.get_active_organizations(GROUPCODE))