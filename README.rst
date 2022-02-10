ShadowTrackr API for Python
===========================

ShadowTrackr is a service that discovers your online attack surface and displays it in a nice graph. Anything found will be monitored for security issues. You can enable notifications by email or push messages, or just ingest them in your SIEM.

All changes to your hosts, websites, certificates, dns and whois records are logged and searchable. Additionally, you can set specific alerts for keywords or events that you want to monitor, for instance a username appearing in leaked data on pastebin.

The API allows you to integrate ShadowTrackr with your other security tools. There are multiple endpoints, but by far the easiest way to gets started is using serach queries. We support both Splunk SPL and Elastic Search (Lucene) syntax thatyou don't have to learn yet another new query language.

More information:

https://test.shadowtrackr.com/docs/2-Data-Model

https://test.shadowtrackr.com/docs/3-Search-and-Queries

Installation::

    pip install shadowtrackr

Usage::

    from shadowtrackr import ShadowTrackr
    from pprint import pprint

    # first, setup the api with your API key
    # you'll find it at: https://shadowtrackr.com/usr/settings?s=api

    st = ShadowTrackr(api_key=API_KEY)

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

    If you need to use a proxy, you can set it like this:

    st.set_proxy("10.0.0.1:8080")

You can find the complete API documentation at https://shadowtrackr.com/docs/5-API

If you have any questions or requests, please send them here: https://shadowtrackr.com/support