import requests
import json


class ShadowTrackr(object):
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://backend.shadowtrackr.com/api/v3/"
        self.proxies = {}

    def set_proxy(self, proxy):
        if proxy.startswith("http://"):
            proxy = proxy[7:]
        elif proxy.startswith("https://"):
            proxy = proxy[8:]
        self.proxies = {"http": "http://" + proxy,
                        "https": "https://" + proxy,
                        }

    def get_timeline(self, update=True, start=None, stop=None, ):
        print("Warning: this function is decprated, use get_events\n")
        postdata = {"api_key": self.api_key, "update": update}
        if start:
            postdata["start"] = start
        if stop:
            postdata["stop"] = stop
        return self.get_data_from_api("timeline", postdata)

    def get_events(self, update=True, start=None, stop=None, ):
        postdata = {"api_key": self.api_key, "update": update}
        if start:
            postdata["start"] = start
        if stop:
            postdata["stop"] = stop
        return self.get_data_from_api("timeline", postdata)


    def get_hosts(self, ip=None, full=None):
        postdata = {"api_key": self.api_key}
        if ip:
            postdata["ip"] = ip
        if full:
            postdata["full"] = True
        return self.get_data_from_api("hosts", postdata)

    def get_websites(self, ip=None, url=None, domain=None, software=None, full=None):
        postdata = {"api_key": self.api_key}
        if ip:
            postdata["ip"] = ip
        if url:
            postdata["url"] = url
        if domain:
            postdata["domain"] = domain
        if software:
            postdata["software"] = software
        if full:
            postdata["full"] = True
        return self.get_data_from_api("websites", postdata)

    def get_certificates(self, ip=None, url=None, domain=None, full=None):
        postdata = {"api_key": self.api_key}
        if ip:
            postdata["ip"] = ip
        if url:
            postdata["url"] = url
        if domain:
            postdata["domain"] = domain
        if full:
            postdata["full"] = True
        return self.get_data_from_api("certificates", postdata)

    def get_phishy_domains(self, domain=None):
        postdata = {"api_key": self.api_key}
        if domain:
            postdata["domain"] = domain
        return self.get_data_from_api("phishy_domains", postdata)

    def get_exposed_email_addresses(self, email=None):
        postdata = {"api_key": self.api_key}
        if email:
            postdata["email"] = email

        return self.get_data_from_api("exposed_email_addresses", postdata)

    def get_suggestions(self):
        postdata = {"api_key": self.api_key}
        return self.get_data_from_api("suggestions", postdata)

    def get_whois(self, url=None, full=None):
        postdata = {"api_key": self.api_key}
        if url:
            postdata["url"] = url
        if full:
            postdata["full"] = True
        return self.get_data_from_api("whois", postdata)

    def get_dns(self, url=None, content=None, record_type=None, full=None):
        postdata = {"api_key": self.api_key}
        if url:
            postdata["url"] = url
        if content:
            postdata["content"] = content
        if record_type:
            postdata["record_type"] = record_type
        if full:
            postdata["full"] = True
        return self.get_data_from_api("dns", postdata)

    def get_urls(self, url=None):
        postdata = {"api_key": self.api_key}
        if url:
            postdata["url"] = url
        return self.get_data_from_api("urls", postdata)

    def get_subnets(self, cidr=None):
        postdata = {"api_key": self.api_key}
        if cidr:
            postdata["cidr"] = cidr
        return self.get_data_from_api("subnets", postdata)

    def get_domains(self, domain=None):
        postdata = {"api_key": self.api_key}
        if domain:
            postdata["domain"] = domain
        return self.get_data_from_api("domains", postdata)

    def get_cloud_providers(self):
        postdata = {"api_key": self.api_key}
        return self.get_data_from_api("cloud_providers", postdata)

    def get_remote_login_services(self):
        postdata = {"api_key": self.api_key}
        return self.get_data_from_api("remote_login_services", postdata)

    def get_assets(self):
        postdata = {"api_key": self.api_key}
        return self.get_data_from_api("assets", postdata)

    def add_assets(self, assets, extract_domains=False):
        postdata = {'api_key': self.api_key, 'assets': assets, 'extract_domains': extract_domains}
        return self.get_data_from_api("add_assets", postdata)

    def remove_assets(self, assets, timeline=True, related=True, include_hosts=True):
        postdata = {'api_key': self.api_key, "assets": assets, "timeline": timeline, "related": related,
                    "include_hosts": include_hosts}
        return self.get_data_from_api("remove_assets", postdata)

    def add_tags(self, assets:list, tags:list, inherit:bool=True):
        postdata = {'api_key': self.api_key, 'assets': assets, 'tags': tags, 'inherit': inherit}
        return self.get_data_from_api("add_tags", postdata)

    def remove_tags(self, assets:list, tags:list, inherit:bool=True):
        postdata = {'api_key': self.api_key, 'assets': assets, 'tags': tags, 'inherit': inherit}
        return self.get_data_from_api("remove_tags", postdata)

    def delete_all_data(self, admincode, save_system_stats=False):
        postdata = {"api_key": self.api_key, "admincode": admincode, "save_system_stats": save_system_stats}
        return self.get_data_from_api("delete_all_my_data", postdata)

    def ignore_urls(self, urls, ignore_subdomains=True):
        postdata = {'api_key': self.api_key, "urls": urls, "ignore_subdomains": ignore_subdomains}
        return self.get_data_from_api("ignore_urls", postdata)

    def unignore_urls(self, urls, unignore_subdomains=True):
        postdata = {'api_key': self.api_key, "urls": urls, "unignore_subdomains": unignore_subdomains}
        return self.get_data_from_api("unignore_urls", postdata)

    def get_software(self):
        postdata = {"api_key": self.api_key}
        return self.get_data_from_api("software", postdata)

    def get_blacklisted_assets(self, ip=None, url=None):
        postdata = {"api_key": self.api_key}
        if ip:
            postdata["ip"] = ip
        if url:
            postdata["url"] = url
        return self.get_data_from_api("blacklisted_assets", postdata)

    def check_initial_scan_progress(self):
        postdata = {"api_key": self.api_key}
        return self.get_data_from_api("initial_scan_progress", postdata)

    def query(self, q):
        postdata = {"api_key": self.api_key, "q": q}
        return self.get_data_from_api("query", postdata)

    def create_organization(self, name, groupcode):
        # you can only use this if you have a multi-tenant account
        postdata = {"api_key": self.api_key, "name": name, "groupcode": groupcode}
        return self.get_data_from_api("create_organization", postdata)

    def get_active_organizations(self, groupcode, full=False):
        # you can only use this if you have a multi-tenant account
        postdata = {"api_key": self.api_key, "groupcode": groupcode, "full": full}
        return self.get_data_from_api("active_organizations", postdata)

    def delete_organization(self, organization_id, groupcode):
        # you can only use this if you have a multi-tenant account
        postdata = {"api_key": self.api_key, "organization_id": organization_id, "groupcode": groupcode}
        return self.get_data_from_api("delete_organization", postdata)

    def get_data_from_api(self, endpoint, postdata):
        response = requests.post(self.base_url + endpoint, data=json.dumps(postdata).encode('utf-8'),
                                 proxies=self.proxies)
        results = json.loads(response.text)
        if 'results' in results and results['results']:
            if isinstance(results['results'], str):
                # go for a nice format
                results['results'] = results['results'].replace("\n", "\n\t")
            else:
                results['results'] = str(results['results'])
        if results["error"]:
            raise Exception(results['error'])
        else:
            return results["data"]
