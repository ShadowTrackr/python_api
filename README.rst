ShadowTrackr API for Python
===========================

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



You can find the complete API documentation at https://shadowtrackr.com/docs/api

If you have any special requests, send them here: https://shadowtrackr.com/support