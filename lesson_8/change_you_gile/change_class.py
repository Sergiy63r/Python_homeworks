import requests


class Change:
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

    def change_project(self, my_id, new_name, new_role):
        payload = {
            "title": new_name,
            "users": {
                "00e51c92-e380-4852-98c2-e696bbe92482": new_role
                }
            }
        head = {
            "Content-Type": "application/json",
            "Authorization": ""    # noqa: E501
            }
        idc = requests.request("PUT", self.url + '/projects/' + my_id, json=payload, headers=head)         # noqa: E501
        return idc.json()

    def project_list(self):
        head = {
            "Content-Type": "application/json",
            "Authorization": ""    # noqa: E501
        }
        list = requests.request("GET", self.url + '/projects', headers=head)
        return list.json()
