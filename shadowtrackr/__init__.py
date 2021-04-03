import requests
import json


class ShadowTrackr(object):
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://shadowtrackr.com/api/v2/"

    def get_timeline(self, update=True, start=None, stop=None, ):
        postdata = {"api_key": self.api_key, "update": update}
        if start:
            postdata["start"] = start
        if stop:
            postdata["stop"] = stop
        response = requests.post(self.base_url + "timeline", data=json.dumps(postdata).encode('utf-8'))
        results = json.loads(response.text)
        if results["error"]:
            raise Exception(results['error'])
        else:
            return results["data"]

    def get_hosts(self, ip=None):
        postdata = {"api_key": self.api_key}
        if ip:
            postdata["ip"] = ip
        response = requests.post(self.base_url + "hosts", data=json.dumps(postdata).encode('utf-8'))
        results = json.loads(response.text)
        if results["error"]:
            raise Exception(results['error'])
        else:
            return results["data"]

    def get_websites(self, ip=None, url=None, domain=None):
        postdata = {"api_key": self.api_key}
        if ip:
            postdata["ip"] = ip
        if url:
            postdata["url"] = url
        if domain:
            postdata["domain"] = domain
        response = requests.post(self.base_url + "websites", data=json.dumps(postdata).encode('utf-8'))
        results = json.loads(response.text)
        if results["error"]:
            raise Exception(results['error'])
        else:
            return results["data"]

    def get_certificates(self, ip=None, url=None, domain=None):
        postdata = {"api_key": self.api_key}
        if ip:
            postdata["ip"] = ip
        if url:
            postdata["url"] = url
        if domain:
            postdata["domain"] = domain
        response = requests.post(self.base_url + "certificates", data=json.dumps(postdata).encode('utf-8'))
        results = json.loads(response.text)
        if results["error"]:
            raise Exception(results['error'])
        else:
            return results["data"]

    def get_phishy_domains(self, domain=None):
        postdata = {"api_key": self.api_key}
        if domain:
            postdata["domain"] = domain
        response = requests.post(self.base_url + "phishy_domains", data=json.dumps(postdata).encode('utf-8'))
        print(response.text)
        results = json.loads(response.text)
        if results["error"]:
            raise Exception(results['error'])
        else:
            return results["data"]

    def get_suggestions(self):
        postdata = {"api_key": self.api_key}
        response = requests.post(self.base_url + "suggestions", data=json.dumps(postdata).encode('utf-8'))
        results = json.loads(response.text)
        if results["error"]:
            raise Exception(results['error'])
        else:
            return results["data"]

    def get_whois(self, url=None):
        postdata = {"api_key": self.api_key}
        if url:
            postdata["url"] = url
        response = requests.post(self.base_url + "whois", data=json.dumps(postdata).encode('utf-8'))
        results = json.loads(response.text)
        if results["error"]:
            raise Exception(results['error'])
        else:
            return results["data"]

    def get_dns(self, url=None, content=None, record_type=None):
        postdata = {"api_key": self.api_key}
        if url:
            postdata["url"] = url
        if content:
            postdata["content"] = content
        if record_type:
            postdata["record_type"] = record_type
        response = requests.post(self.base_url + "dns", data=json.dumps(postdata).encode('utf-8'))
        results = json.loads(response.text)
        if results["error"]:
            raise Exception(results['error'])
        else:
            return results["data"]

    def get_urls(self, url=None):
        postdata = {"api_key": self.api_key}
        if url:
            postdata["url"] = url
        response = requests.post(self.base_url + "urls", data=json.dumps(postdata).encode('utf-8'))
        results = json.loads(response.text)
        if results["error"]:
            raise Exception(results['error'])
        else:
            return results["data"]

    def get_cloud_providers(self):
        postdata = {"api_key": self.api_key}
        response = requests.post(self.base_url + "cloud_providers", data=json.dumps(postdata).encode('utf-8'))
        results = json.loads(response.text)
        if results["error"]:
            raise Exception(results['error'])
        else:
            return results["data"]

    def get_remote_login_services(self):
        postdata = {"api_key": self.api_key}
        response = requests.post(self.base_url + "remote_login_services", data=json.dumps(postdata).encode('utf-8'))
        results = json.loads(response.text)
        if results["error"]:
            raise Exception(results['error'])
        else:
            return results["data"]

    def get_graph(self, delay=None, name=None):
        postdata = {"api_key": self.api_key}
        if delay:
            postdata["delay"] = delay
        if name:
            postdata["content"] = name
        response = requests.post(self.base_url + "graph", data=json.dumps(postdata).encode('utf-8'))
        if response.status_code == 200:
            return response.content
        results = json.loads(response.text)
        if results["error"]:
            raise Exception(results['error'])
        else:
            return results["data"]

    def get_assets(self):
        postdata = {"api_key": self.api_key}
        response = requests.post(self.base_url + "assets", data=json.dumps(postdata).encode('utf-8'))
        results = json.loads(response.text)
        if results["error"]:
            raise Exception(results['error'])
        else:
            return results["data"]

    def add_assets(self, assets):
        postdata = {'api_key': self.api_key, 'assets': assets}
        response = requests.post(self.base_url + "add_assets", data=json.dumps(postdata).encode('utf-8'))
        results = json.loads(response.text)
        if results["error"]:
            raise Exception(results['error'])
        else:
            return results["data"]

    def remove_assets(self, assets, timeline=True, related=True, include_hosts=True):
        postdata = {'api_key': self.api_key, "assets": assets, "timeline": timeline, "related": related,
                    "include_hosts": include_hosts}
        response = requests.post(self.base_url + "remove_assets", data=json.dumps(postdata).encode('utf-8'))
        results = json.loads(response.text)
        if results["error"]:
            raise Exception(results['error'])
        else:
            return results["data"]

    def delete_all_data(self, admincode):
        postdata = {"api_key": self.api_key, "admincode": admincode}
        response = requests.post(self.base_url + "delete_all_my_data", data=json.dumps(postdata).encode('utf-8'))
        results = json.loads(response.text)
        if results["error"]:
            raise Exception(results['error'])
        else:
            return results["data"]

    def ignore_urls(self, urls, ignore_subdomains=True):
        postdata = {'api_key': self.api_key, "urls": urls, "ignore_subdomains": ignore_subdomains}
        response = requests.post(self.base_url + "ignore_urls", data=json.dumps(postdata).encode('utf-8'))
        results = json.loads(response.text)
        if results["error"]:
            raise Exception(results['error'])
        else:
            return results["data"]

    def unignore_urls(self, urls, unignore_subdomains=True):
        postdata = {'api_key': self.api_key, "urls": urls, "unignore_subdomains": unignore_subdomains}
        response = requests.post(self.base_url + "unignore_urls", data=json.dumps(postdata).encode('utf-8'))
        results = json.loads(response.text)
        if results["error"]:
            raise Exception(results['error'])
        else:
            return results["data"]
