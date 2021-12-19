import requests


def test_current_drivers_list_api_incorrect_response():
    url = "https://ergast.com/api/f1/curent/drivers.json"
    r = requests.get(url)
    assert r.status_code == 400
