import requests
import json


class ShadowTrackr(object):
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://shadowtrackr.com/api/v2/"

    def get_timeline(self):
        postdata = {"api_key": self.api_key}
        response = requests.post(self.base_url + "timeline", data=json.dumps(postdata).encode('utf-8'))
        print(response.text)
        results = json.loads(response.text)
        if results["error"]:
            raise Exception(results['error'])
        else:
            return results["data"]

    def get_hosts(self):
        postdata = {"api_key": self.api_key}
        response = requests.post(self.base_url + "hosts", data=json.dumps(postdata).encode('utf-8'))
        results = json.loads(response.text)
        if results["error"]:
            raise Exception(results['error'])
        else:
            return results["data"]

    def get_websites(self):
        postdata = {"api_key": self.api_key}
        response = requests.post(self.base_url + "websites", data=json.dumps(postdata).encode('utf-8'))
        results = json.loads(response.text)
        if results["error"]:
            raise Exception(results['error'])
        else:
            return results["data"]

    def get_certificates(self):
        postdata = {"api_key": self.api_key}
        response = requests.post(self.base_url + "certificates", data=json.dumps(postdata).encode('utf-8'))
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

    def get_whois(self):
        postdata = {"api_key": self.api_key}
        response = requests.post(self.base_url + "whois", data=json.dumps(postdata).encode('utf-8'))
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

    def remove_assets(self, assets):
        postdata = {'api_key': self.api_key, 'assets': assets}
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


