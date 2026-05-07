from shadowtrackr import ShadowTrackr
from time import sleep

API_KEY = "CHANGEME"
ADMINCODE = "CHANGEME"

st = ShadowTrackr(api_key=API_KEY)

###
# CAUTION: only uncomment this if you know what you are doing.
# It will delete ALL your assets and you'll start with a clean slate.
#st.delete_all_my_data(admincode=ADMINCODE)

# Add some assets to seed the discovery. You can mix and match urls and ips
assets = ["www.shadowtrackr.com", "91.98.127.83"]

# The extract domains flag will extract shadowtrackr.com and add it too. You get the same effect if you just
# add shadowtrackr.com. If you only add the subdomain url www.shadowtrackr.com and not set this flag,
# the domain shadowtrackr.com will NOT be added
st.add_assets(assets, extract_domains=True)

# Now allow some time to discover assets
i = 20  # We should have some data to play with after 30m
while i > 0:
    sleep(60)
    status = st.initial_scan_progress()
    print(status)
    # This is the "popcorn" method. If no new assets are popping up, then the first round of scanning must be done.
    # Note that after this ShadowTrackr will continuously keep scanning your assets.
    # New assets might be found tomorrow or next week
    data = status.get("data")
    if data and i > 5 and data.get("total_assets", 0) > 0 and data.get("scan_activity_in_last_5m") == 0:
        break
    i -= 1

hosts = st.hosts()
websites = st.websites()
certificates = st.certificates()
suggestions = st.suggestions()
dns = st.dns()
domains = st.domains()

print("Initial scan on ShadowTrackr found: ")
print("Hosts: " + str(len(hosts['data'])))
print("Websites: " + str(len(websites['data'])))
print("Certificates: " + str(len(certificates['data'])))
print("Dns records: " + str(len(dns['data'])))
print("Domains: " + str(len(domains['data'])))


# You can ignore urls. Some will keep getting discovered after you delete them because they're tied to your
# infrastructure. If you really want to exclude those from monitoring and reports, ignoring is the way to go.
# Set the subdomain flag to make sure any current and future subdomains will be ignored too
#urls = ["shadowtrackr.com"]
#st.ignore_urls(urls, ignore_subdomains=True)