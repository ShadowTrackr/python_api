from shadowtrackr import ShadowTrackr
from time import sleep
from PIL import Image
from io import BytesIO


API_KEY = "ddb41951a4d2c61df93346fa9037f029"
ADMINCODE = "87687bdb86ad1b1581ab39f9c198cbd4"

st = ShadowTrackr(api_key=API_KEY)

###
# CAUTION: only uncomment this if you know what you are doing.
# It will delete ALL your assets and you'll start with a clean slate.
#st.delete_all_data(admincode=ADMINCODE)

# Add some assets to seed the discovery. You can mix and match urls and ips
assets = ["shadowtrackr.com", "139.162.214.30"]
st.add_assets(assets)

# Now allow some time to discover assets
i = 15  # We should have some data to play with after 30m, so bail out
while i > 0:
    sleep(60)
    status = st.check_initial_scan_progress()
    print(status)
    # This is the "popcorn" method. If no new assets are popping up, then the first round of scanning must be done.
    # Note that after this ShadowTrackr will continuously keep scanning your assets.
    # New assets might be found tomorrow or next week
    if i > 5 and status.get("total_assets") > 0 and status.get("scan_activity_in_last_5m") == 0:
        break
    i -= 1

hosts = st.get_hosts()
websites = st.get_websites()
certificates = st.get_certificates()
suggestions = st.get_suggestions()
dns = st.get_dns()

print("Initial scan on ShadowTrackr found: ")
print("Hosts (should be >= 4): " + str(len(hosts)))
print("Websites (should be >= 6 ): " + str(len(websites)))
print("Certificates (should be >= 4): " + str(len(certificates)))
print("Dns records (should be >= 15): " + str(len(dns)))

# now get your Attack Surface Graph as a png file
img = Image.open(BytesIO(st.get_graph()))
img.save("Attack Surface Graph.png", "PNG")

# You can ignore urls. Some will keep getting discovered after you delete them because they're tied to your
# infrastructure. If you really want to exclude those from monitoring and reports, ignoring is the way to go.
# Set the subdomain flag to make sure any current and future subdomains will be ignored too
#urls = ["shadowtrackr.com"]
#st.ignore_urls(urls, ignore_subdomains=True)
