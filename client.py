import requests


base_url = "http://chrisbrooks.pythonanywhere.com/"


def get_programmer_count():
    r = requests.get(base_url + 'api/programmers')
    programmers = r.json()
    return len(programmers['programmers'])


def get_programmer_by_id(pid):
    r = requests.get(base_url + f"api/programmers/{pid}")
    if r.status_code == 200:
        return r.json()
    else:
        return {}
        # return None


def get_full_name_from_first(first_name):
    r = requests.get(base_url + f"api/programmers/by_first_name/{first_name}")
    programmer_list = r.json()['programmers']
    if len(programmer_list) == 0:
        return None
    else:
        return programmer_list[0]['first'] + " " + programmer_list[0]['last']
