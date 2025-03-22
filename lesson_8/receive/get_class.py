import requests


class Receive:
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

    def project_list_id(self, my_id):
        head = {
            "Content-Type": "application/json",
            "Authorization": ""    # noqa: E501
        }
        list = requests.request("GET", self.url + '/projects/' + my_id, headers=head)                       # noqa: E501
        return list.json()

    def get_list_id(self, id):
        headers = {
          "Content-Type": "application/json",
          "Authorization": ""      # noqa: E501
        }

        list_id = requests.request("GET", self.url + '/projects/' + id, headers=headers)                    # noqa: E501
        return list_id.json()
