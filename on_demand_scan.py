from shadowtrackr import ShadowTrackr
from time import sleep
from PIL import Image
from io import BytesIO



API_KEY = "ddb41951a4d2c61df93346fa9037f029"
ADMINCODE = "87687bdb86ad1b1581ab39f9c198cbd4"

st = ShadowTrackr(api_key=API_KEY)

# delete all old data first
st.delete_all_data(admincode=ADMINCODE)

# add new assets
assets = ["shadowtrackr.com"]
st.add_assets(assets)

# allow some time to discover assets
sleep(15*60)

# Instead, you could also use the popcorn method:
# periodically (say, each 60s) you call st.get_assets()
# if the number of assets stops changing your scan is done.


hosts = st.get_hosts()
websites = st.get_websites()
certificates = st.get_certificates()
suggestions = st.get_suggestions()
dns = st.get_dns()

print("Initial scan on ShadowTrackr found: ")
print("Hosts (should be 4): " + str(len(hosts)))
print("Websites (should be 8): " + str(len(websites)))
print("Certificates (should be 4): " + str(len(certificates)))
print("Dns records (should be 15): " + str(len(dns)))

# now get your Attack Surface Graph as a png file
img = Image.open(BytesIO(st.get_graph()))
img.save("Attack Surface Graph.png", "PNG")

# how to ignore urls
# the subdomain flag make sure any current and newly found subdomain will be ignored too
urls = ["shadowtrackr.com"]
st.ignore_urls(urls, ignore_subdomains=True)