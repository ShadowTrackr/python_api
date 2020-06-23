from shadowtrackr import ShadowTrackr
from time import sleep


API_KEY = "e03601b4f80b5439dfd73638e2a15957"
ADMINCODE = "a4b873208f3e43a9624cfc16b55a8350"

st = ShadowTrackr(api_key=API_KEY)

# delete all old data first
st.delete_all_data(admincode=ADMINCODE)

# add new assets

assets = ["politie.nl", "shadowtrackr.com"]
st.add_assets(assets)

sleep(15*60)

hosts = st.get_hosts()
websites = st.get_websites()
certificates = st.get_certificates()
suggestions = st.get_suggestions()

print("Initial scan on ShadowTrackr found: ")
print("Hosts: " + str(len(hosts)))
print("Websites: " + str(len(hosts)))
print("Certificates: " + str(len(certificates)))

# show all certificate problems found:
for c in websites:
    if c["problems"]:
        print(c["url"] + " has problems:")
        for p in c["problems"]:
            print(p)
        print("\n")


