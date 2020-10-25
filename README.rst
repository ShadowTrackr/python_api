ShadowTrackr API for Python
===========================

ShadowTrackr is a service that discovers your online attack surface and displays it in a nice graph. Anything found will be monitored for security issues. You can enable notifications by email or push messages, or just ingest them in your SIEM.

All changes to your hosts, websites, certificates, dns and whois records are logged and searchable. Additionally, you can set specific traps for keywords or events that you want to monitor, for instance a username appearing in leaked data on pastebin.

The API allows you to integrate ShadowTrackr with your other security tools. This is a python package to simplify integration.

Installation::

    pip install shadowtrackr

Usage::

    from shadowtrackr import ShadowTrackr
    from time import sleep

    # first, setup the api with your API key
    # you'll find it at: https://shadowtrackr.com/usr/settings?s=api

    st = ShadowTrackr(api_key=API_KEY)

    # add some assets as a starting point

    assets = ["shadowtrackr.com", "vanschaik-ltd.com", "139.162.214.30"]
    st.add_assets(assets)

    # now give ST about 15 minutes for initial discovery
    sleep(15*60)

    # get your results
    host = st.get_hosts()
    websites = st.get_websites()
    certificates = st.get_certificates()

    # show all certificate problems found:
    for c in certificates:
        if c["problems"]:
            print(c["url"] + " has problems:")
            for p in c["problems"]:
                print(p)
            print("\n")

Get a PNG version of a network graph::

    from shadowtrackr import ShadowTrackr
    from io import BytesIO
    from PIL import Image
    # note that you might have to do this first: pip install pillow

    st = ShadowTrackr(api_key=API_KEY)
    img = Image.open(BytesIO(st.get_graph(name="Attack surface")))
    img.save("Attack Surface Graph.png", "PNG")


You can find the complete API documentation at https://shadowtrackr.com/docs/api

If you have any questions or requests, please send them here: https://shadowtrackr.com/support