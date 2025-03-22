import requests


class Create:
    def __init__(self, url):
        self.url = url

    def new_project(self, names, roles):
        payload = {
            "title": names,
            "users": {
                "00e51c92-e380-4852-98c2-e696bbe92482": roles
                }
            }
        head = {
            "Content-Type": "application/json",
            "Authorization": ""    # noqa: E501
        }
        req = requests.request("POST", self.url + '/projects', json=payload, headers=head)                # noqa: E501
        return req.json()

    def new_project_id(self):
        head = {
            "Content-Type": "application/json",
            "Authorization": ""     # noqa: E501
        }
        idp = requests.request("GET", self.url + '/projects', headers=head)
        return idp.json()
