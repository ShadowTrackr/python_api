from shadowtrackr import ShadowTrackr
from pprint import pprint

API_KEY = "ddb41951a4d2c61df93346fa9037f029"
ADMINCODE = "87687bdb86ad1b1581ab39f9c198cbd4"

st = ShadowTrackr(api_key=API_KEY)

# More information about the Data Model and Query language::
# https://test.shadowtrackr.com/docs/2-Data-Model
# https://test.shadowtrackr.com/docs/3-Search-and-Queries

certificate_issuers = st.query("index=certificates by issuer earliest=-10d")
pprint(certificate_issuers)

problem_hosts = st.query("index=hosts problem=yes earliest=-1m")
pprint(problem_hosts)

hosts_with_rdp_open = st.query("index=hosts ports=3389")
pprint(hosts_with_rdp_open)

all_spf_records = st.query("index=dns rrtype=txt rrdata=\"*spf*\"")
pprint(all_spf_records)

websites_on_nginx = st.query("index=websites https_server=*nginx*")
pprint(websites_on_nginx)

good_certificates = st.query("index=certificates grade=A earliest=-1m")
pprint(good_certificates)

all_whois_records = st.query("index=whois")
pprint(all_whois_records)