import requests


def get_data():
    url = "https://cat-fact.herokuapp.com/facts"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    #print(response.text)
    return response.json()
