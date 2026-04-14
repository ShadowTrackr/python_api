from shadowtrackr import ShadowTrackr
import json

API_KEY = "CHANGEME"
ADMINCODE = "CHANGEME"

st = ShadowTrackr(api_key=API_KEY)

# More information about the Data Model and Query language::
# https://shadowtrackr.com/docs/

print("# Certificate Issuers")
certificate_issuers = st.query("index=certificates by issuer earliest=-10d")
print(json.dumps(certificate_issuers, indent=2))
print("###\n")

print("# Problem hosts")
problem_hosts = st.query("index=hosts problem=true earliest=-1m")
print(json.dumps(problem_hosts, indent=2))
print("###\n")

print("# Hosts with RDP open")
hosts_with_rdp_open = st.query("index=hosts ports=3389")
print(json.dumps(hosts_with_rdp_open, indent=2))
print("###\n")

print("# DNS SPF Records")
all_spf_records = st.query("index=dns rrtype=txt rrdata=\"*spf*\"")
print(json.dumps(all_spf_records, indent=2))
print("###\n")

print("# Websites running nginx")
websites_on_nginx = st.query("index=websites https_server=*nginx*")
print(json.dumps(websites_on_nginx, indent=2))
print("###\n")

print("# Good certificates")
good_certificates = st.query("index=certificates grade=A earliest=-1m")
print(json.dumps(good_certificates, indent=2))
print("###\n")
