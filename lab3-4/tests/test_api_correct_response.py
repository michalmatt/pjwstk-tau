import requests


def test_current_drivers_list_api_correct_response():
    url = "https://ergast.com/api/f1/current/drivers.json"
    r = requests.get(url)
    assert r.status_code == 200
