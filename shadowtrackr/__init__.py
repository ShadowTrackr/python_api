import requests
import json


class ShadowTrackr(object):
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.shadowtrackr.com/api/"
        self.proxies = {}
        self.api_v3 = False

    def set_proxy(self, proxy: str):
        if proxy.startswith("http://"):
            proxy = proxy[7:]
        elif proxy.startswith("https://"):
            proxy = proxy[8:]
        self.proxies = {"http": "http://" + proxy,
                        "https": "https://" + proxy,
                        }
    def set_api_v3(self):
        print("Warning: API v3 sucks compared to v4. Try v4!\n")
        self.api_v3 = True

    def query(self, q: str):
        if self.api_v3:
            postdata = {"api_key": self.api_key, "q": q}
            return self.get_data_from_api_v3("query", postdata)
        else:
            postdata = {"q": q}
            return self.get_data_from_api("query", postdata)

    def get_timeline(self, update: bool = True, start: str = None, stop: str = None, ):
        if not self.api_v3:
            print("Warning: this function is deprecated, use st.events()\n")
        postdata = {"api_key": self.api_key, "update": update}
        if start:
            postdata["start"] = start
        if stop:
            postdata["stop"] = stop
        return self.get_data_from_api_v3("timeline", postdata)

    def get_events(self, update: bool = True, start: str = None, stop: str = None):
        if not self.api_v3:
            print("Warning: this function is deprecated, use st.events()\n")
        postdata = {"api_key": self.api_key, "update": update}
        if start:
            postdata["start"] = start
        if stop:
            postdata["stop"] = stop
        return self.get_data_from_api_v3("timeline", postdata)

    def events(self, update_only: bool = True, start: str = None, stop: str = None, output_format: str = "json"):
        postdata = {"update": update_only}
        if start:
            postdata["start"] = start
        if stop:
            postdata["stop"] = stop
        if output_format:
            postdata["output_format"] = output_format
        return self.get_data_from_api("events", postdata)

    def get_mailservers(self):
        if not self.api_v3:
            print("Warning: this function is deprecated, use st.mailservers()\n")
        postdata = {"api_key": self.api_key}
        return self.get_data_from_api_v3("mailservers", postdata)

    def mailservers(self):
        return self.get_data_from_api("mailservers", {})

    def get_hosts(self, ip: str = None, full: bool = False):
        if not self.api_v3:
            print("Warning: this function is deprecated, use st.hosts()\n")
        postdata = {"api_key": self.api_key}
        if ip:
            postdata["ip"] = ip
        if full:
            postdata["full"] = True
        return self.get_data_from_api_v3("hosts", postdata)

    def hosts(self, ip: str = None, full: bool = False):
        postdata = {}
        if ip:
            postdata["ip"] = ip
        if full:
            postdata["full"] = True
        return self.get_data_from_api("hosts", postdata)

    def get_websites(self, ip: str = None, url: str = None, domain: str = None, full: bool = False):
        if not self.api_v3:
            print("Warning: this function is deprecated, use st.websites()\n")
        postdata = {"api_key": self.api_key}
        if ip:
            postdata["ip"] = ip
        if url:
            postdata["url"] = url
        if domain:
            postdata["domain"] = domain
        if full:
            postdata["full"] = True
        return self.get_data_from_api_v3("websites", postdata)

    def websites(self, ip: str = None, url: str = None, domain: str = None, full: bool = False):
        postdata = {}
        if ip:
            postdata["ip"] = ip
        if url:
            postdata["url"] = url
        if domain:
            postdata["domain"] = domain
        if full:
            postdata["full"] = True
        return self.get_data_from_api("websites", postdata)

    def get_certificates(self, ip: str = None, url: str = None, domain: str = None, full: bool = False):
        if not self.api_v3:
            print("Warning: this function is deprecated, use st.certificates()\n")
        postdata = {"api_key": self.api_key}
        if ip:
            postdata["ip"] = ip
        if url:
            postdata["url"] = url
        if domain:
            postdata["domain"] = domain
        if full:
            postdata["full"] = True
        return self.get_data_from_api_v3("certificates", postdata)

    def certificates(self, ip: str = None, url: str = None, domain: str = None, full: bool = False):
        postdata = {}
        if ip:
            postdata["ip"] = ip
        if url:
            postdata["url"] = url
        if domain:
            postdata["domain"] = domain
        if full:
            postdata["full"] = True
        return self.get_data_from_api("certificates", postdata)

    def get_dns(self, url: str = None, content: str = None, record_type: str = None):
        if not self.api_v3:
            print("Warning: this function is deprecated, use st.dns()\n")
        postdata = {"api_key": self.api_key}
        if url:
            postdata["url"] = url
        if content:
            postdata["content"] = content
        if record_type:
            postdata["record_type"] = record_type
        return self.get_data_from_api_v3("dns", postdata)

    def dns(self, url: str = None, rrdata: str = None, rrtype: str = None):
        postdata = {}
        if url:
            postdata["url"] = url
        if rrdata:
            postdata["rrdata"] = rrdata
        if rrtype:
            postdata["rrtype"] = rrtype
        return self.get_data_from_api("dns", postdata)

    def get_domains(self, domain: str = None):
        if not self.api_v3:
            print("Warning: this function is deprecated, use st.domains()\n")
        postdata = {"api_key": self.api_key}
        if domain:
            postdata["domain"] = domain
        return self.get_data_from_api_v3("domains", postdata)

    def domains(self, domain: str = None):
        postdata = {}
        if domain:
            postdata["domain"] = domain
        return self.get_data_from_api("domains", postdata)

    def get_urls(self, url: str = None):
        if not self.api_v3:
            print("Warning: this function is deprecated, use st.urls()\n")
        postdata = {"api_key": self.api_key}
        if url:
            postdata["url"] = url
        return self.get_data_from_api_v3("urls", postdata)

    def urls(self, url: str = None):
        postdata = {}
        if url:
            postdata["url"] = url
        return self.get_data_from_api("urls", postdata)

    def get_subnets(self, cidr: str = None):
        if not self.api_v3:
            print("Warning: this function is deprecated, use st.subnets()\n")
        postdata = {"api_key": self.api_key}
        if cidr:
            postdata["cidr"] = cidr
        return self.get_data_from_api_v3("subnets", postdata)

    def subnets(self, cidr: str = None):
        postdata = {}
        if cidr:
            postdata["cidr"] = cidr
        return self.get_data_from_api("subnets", postdata)

    def get_cloud_providers(self):
        if not self.api_v3:
            print("Warning: this function is deprecated, use st.cloud_providers()\n")
        postdata = {"api_key": self.api_key}
        return self.get_data_from_api_v3("cloud_providers", postdata)

    def cloud_providers(self):
        postdata = {}
        return self.get_data_from_api("cloud_providers", postdata)

    def get_remote_login_services(self):
        if not self.api_v3:
            print("Warning: this function is deprecated, use st.remote_login_services()\n")
        postdata = {"api_key": self.api_key}
        return self.get_data_from_api_v3("remote_login_services", postdata)

    def remote_login_services(self):
        postdata = {}
        return self.get_data_from_api("remote_login_services", postdata)

    def get_phishy_domains(self, domain: str = None):
        if not self.api_v3:
            print("Warning: this function is deprecated, use st.phishy_domains()\n")
        postdata = {"api_key": self.api_key}
        if domain:
            postdata["domain"] = domain
        return self.get_data_from_api_v3("phishy_domains", postdata)

    def phishy_domains(self, domain: str = None):
        postdata = {}
        if domain:
            postdata["domain"] = domain
        return self.get_data_from_api("phishy_domains", postdata)

    def get_exposed_email_addresses(self, email: str = None):
        if not self.api_v3:
            print("Warning: this function is deprecated, use st.exposed_email_addresses()\n")
        postdata = {"api_key": self.api_key}
        if email:
            postdata["email"] = email
        return self.get_data_from_api_v3("exposed_email_addresses", postdata)

    def exposed_email_addresses(self, email: str = None):
        postdata = {}
        if email:
            postdata["email"] = email
        return self.get_data_from_api("exposed_email_addresses", postdata)

    def get_suggestions(self):
        if not self.api_v3:
            print("Warning: this function is deprecated, use st.suggestions()\n")
        postdata = {"api_key": self.api_key}
        return self.get_data_from_api_v3("suggestions", postdata)

    def suggestions(self):
        postdata = {}
        return self.get_data_from_api("suggestions", postdata)

    def get_whois(self, url: str = None, full: bool = False):
        if not self.api_v3:
            print("Warning: this function is deprecated, use st.domains()\n")
        postdata = {"api_key": self.api_key}
        if url:
            postdata["url"] = url
        if full:
            postdata["full"] = True
        return self.get_data_from_api_v3("whois", postdata)

    def get_blacklisted_assets(self, ip: str = None, url: str = None):
        if not self.api_v3:
            print("Warning: this function is deprecated, use st.blacklisted_assets()\n")
        postdata = {"api_key": self.api_key}
        if ip:
            postdata["ip"] = ip
        if url:
            postdata["url"] = url
        return self.get_data_from_api_v3("blacklisted_assets", postdata)

    def blacklisted_assets(self, ip: str = None, url: str = None):
        postdata = {}
        if ip:
            postdata["ip"] = ip
        if url:
            postdata["url"] = url
        return self.get_data_from_api("blacklisted_assets", postdata)

    def get_software(self):
        if not self.api_v3:
            print("Warning: this function is deprecated, use st.software()\n")
        postdata = {"api_key": self.api_key}
        return self.get_data_from_api_v3("software", postdata)

    def software(self):
        postdata = {}
        return self.get_data_from_api("software", postdata)

    def vulnerabilities(self):
        postdata = {}
        return self.get_data_from_api("vulnerabilities", postdata)

    def suppliers(self):
        postdata = {}
        return self.get_data_from_api("suppliers", postdata)

    def get_assets(self):
        if not self.api_v3:
            print("Warning: this function is deprecated, use st.assets()\n")
        postdata = {"api_key": self.api_key}
        return self.get_data_from_api_v3("assets", postdata)

    def assets(self):
        postdata = {}
        return self.get_data_from_api("assets", postdata)

    def add_assets(self, assets: list[str], extract_domains: bool = False):
        if self.api_v3:
            postdata = {"api_key": self.api_key, "assets": assets, "extract_domains": extract_domains}
            return self.get_data_from_api_v3("add_assets", postdata)
        else:
            postdata = {"assets": assets, "extract_domains": extract_domains}
            return self.get_data_from_api("add_assets", postdata)

    def remove_assets(self, assets: list[str], timeline: bool = True, related: bool = True, include_hosts: bool = True):
        if not self.api_v3:
            print("Warning: this function is deprecated, use st.delete_assets()\n")
        postdata = {"api_key": self.api_key, "assets": assets, "timeline": timeline, "related": related,
                    "include_hosts": include_hosts}
        return self.get_data_from_api_v3("remove_assets", postdata)

    def delete_assets(self, assets: list[str], timeline: bool = True, related: bool = True, include_hosts: bool = True):
            postdata = {"assets": assets, "timeline": timeline, "related": related,
                        "include_hosts": include_hosts}
            return self.get_data_from_api("delete_assets", postdata)

    def add_tags(self, assets: list[str], tags: list[str], inherit: bool = True):
        if self.api_v3:
            postdata = {"api_key": self.api_key, "assets": assets, "tags": tags, "inherit": inherit}
            return self.get_data_from_api_v3("add_tags", postdata)
        else:
            postdata = {"assets": assets, "tags": tags, "inherit": inherit}
            return self.get_data_from_api("add_tags", postdata)

    def remove_tags(self, assets: list[str], tags: list[str], inherit: bool = True):
        if not self.api_v3:
            print("Warning: this function is deprecated, use st.delete_tags()\n")
        postdata = {"api_key": self.api_key, "assets": assets, "tags": tags, "inherit": inherit}
        return self.get_data_from_api_v3("remove_tags", postdata)

    def delete_tags(self, assets: list[str], tags: list[str], inherit: bool = True):
        postdata = {"assets": assets, "tags": tags, "inherit": inherit}
        return self.get_data_from_api("delete_tags", postdata)

    def ignore_urls(self, urls: list[str], ignore_subdomains: bool = True):
        if self.api_v3:
            postdata = {"api_key": self.api_key, "urls": urls, "ignore_subdomains": ignore_subdomains}
            return self.get_data_from_api_v3("ignore_urls", postdata)
        else:
            postdata = {"urls": urls, "ignore_subdomains": ignore_subdomains}
            return self.get_data_from_api("ignore_urls", postdata)

    def unignore_urls(self, urls: list[str], unignore_subdomains: bool = True):
        if self.api_v3:
            postdata = {"api_key": self.api_key, "urls": urls, "unignore_subdomains": unignore_subdomains}
            return self.get_data_from_api_v3("unignore_urls", postdata)
        else:
            postdata = {"urls": urls, "unignore_subdomains": unignore_subdomains}
            return self.get_data_from_api("unignore_urls", postdata)

    def delete_all_data(self, admincode: str, save_system_stats: bool = False):
        if not self.api_v3:
            print("Warning: this function is deprecated, use st.delete_all_my_data()\n")
        postdata = {"api_key": self.api_key, "admincode": admincode, "save_system_stats": save_system_stats}
        return self.get_data_from_api_v3("delete_all_my_data", postdata)

    def delete_all_my_data(self, admincode: str, save_system_stats: bool = False):
        postdata = {"admincode": admincode, "save_system_stats": save_system_stats}
        return self.get_data_from_api("delete_all_my_data", postdata)

    def check_initial_scan_progress(self):
        if not self.api_v3:
            print("Warning: this function is deprecated, use st.initial_scan_progress()\n")
        postdata = {"api_key": self.api_key}
        return self.get_data_from_api_v3("initial_scan_progress", postdata)

    def initial_scan_progress(self):
        postdata = {}
        return self.get_data_from_api("initial_scan_progress", postdata)

    def scannernode_ip_addresses(self):
        postdata = {}
        return self.get_data_from_api("scannernode_ip_addresses", postdata)

    def ip_info(self, ip: str = None):
        postdata = {"ip": ip}
        return self.get_data_from_api("ip_info", postdata)

    def create_organization(self, name: str, groupcode: str):
        # you can only use this if you have a multi-tenant account
        if not self.api_v3:
            print("Warning: this function is deprecated, use st.add_organization()\n")
        postdata = {"api_key": self.api_key, "name": name, "groupcode": groupcode}
        return self.get_data_from_api_v3("create_organization", postdata)

    def add_organization(self, name: str, groupcode: str):
        postdata = {"name": name, "groupcode": groupcode}
        return self.get_data_from_api("add_organization", postdata)

    def get_active_organizations(self, groupcode: str, full: bool = False):
        # you can only use this if you have a multi-tenant account
        if not self.api_v3:
            print("Warning: this function is deprecated, use st.organizations()\n")
        postdata = {"api_key": self.api_key, "groupcode": groupcode, "full": full}
        return self.get_data_from_api_v3("active_organizations", postdata)

    def organizations(self, groupcode: str):
        postdata = {"groupcode": groupcode}
        return self.get_data_from_api("organizations", postdata)

    def delete_organization(self, organization_id: int = None, groupcode: str = None, oid: int = None):
        # you can only use this if you have a multi-tenant account
        if self.api_v3:
            if not organization_id and oid:
                raise Exception("You need to use organization_id for API v3, not oid.")
            postdata = {"api_key": self.api_key, "organization_id": organization_id, "groupcode": groupcode}
            return self.get_data_from_api_v3("delete_organization", postdata)
        else:
            if organization_id and not oid:
                raise Exception("You need to use oid for API v4, not organization_id.")
            postdata = {"oid": oid, "groupcode": groupcode}
            return self.get_data_from_api("delete_organization", postdata)

    def get_data_from_api_v3(self, endpoint: str, postdata: dict):
        response = requests.post(self.base_url + "v3/" + endpoint, data=json.dumps(postdata).encode("utf-8"),
                                 proxies=self.proxies)
        results = json.loads(response.text)
        if "results" in results and results["results"]:
            if isinstance(results["results"], str):
                # go for a nice format
                results["results"] = results["results"].replace("\n", "\n\t")
            else:
                results["results"] = str(results["results"])
        if results["error"]:
            raise Exception(results["error"])
        else:
            return results["data"]

    def get_data_from_api(self, endpoint: str, postdata: dict):
        response = requests.post(self.base_url + "v4/" + endpoint,
                                 data=json.dumps(postdata).encode("utf-8"),
                                 headers={"Authorization": f"Bearer {self.api_key}"},
                                 proxies=self.proxies)
        if not response.ok:
            print(f"HTTP Error {response.status_code}: {response.text}")
            return None
        if endpoint == "events" and "CEF:0|ShadowTrackr|API feed|1.0|" in response.text:
            return response.text
        results = json.loads(response.text)
        return results

