import requests


def test_current_drivers_keys_values():
    expected = ['series', 'url', 'DriverTable']
    current = []
    url = "https://ergast.com/api/f1/current/drivers.json"
    r = requests.get(url)
    data = r.json()
    for key, value in data.items():
        for k, v in value.items():
            if k in expected:
                current.append(k)
    assert expected == current

