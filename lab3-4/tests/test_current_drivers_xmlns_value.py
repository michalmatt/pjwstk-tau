import requests


def test_current_drivers_xmlns_value():
    url = "https://ergast.com/api/f1/current/drivers.json"
    r = requests.get(url)
    data = r.json()
    for key, value in data.items():
        for k, v in value.items():
            if k == 'xmlns':
                xmlns = v

    assert xmlns == 'http://ergast.com/mrd/1.4'

