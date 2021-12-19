"""
==========================================================
Ergast Developer API usage & testing
==========================================================
Author (of the code below, not the API): Michal Matusiak
API documentation: http://ergast.com/mrd/

List of functions divided into categories
----------------------------------------------------------
1) UTC date & time
get_current_date_utc() - returns current utc date in yyyy-mm-dd format
get_current_time_utc() - returns current utc time in hh-mm-ss format

2) F1 races info
get_current_race_list() - gets F1 races data for current year (from external API)
get_race_remaining_time_today() - if race is planned for today returns remaining time, if not returns: None

3) F1 drivers info
get_current_drivers_list() - gets F1 drivers info for current year (from external API)
"""


import requests
from datetime import datetime


def get_current_date_utc():
    return datetime.utcnow().strftime("%Y-%m-%d")


def get_current_time_utc():
    return datetime.utcnow().strftime("%H:%M:%S")


def get_current_races_list():
    url = "http://ergast.com/api/f1/current.json"
    r = requests.get(url)
    data = r.json()
    races_list = data['MRData']['RaceTable']['Races']
    return races_list


def get_race_remaining_time_today():
    races_list = get_current_races_list()
    current_date = get_current_date_utc()
    current_time = get_current_time_utc()
    remaining_time = None
    fmt = '%H:%M:%S'
    for x in races_list:
        if x['date'] == current_date:
            race_time = x['time'].replace('Z', '')
            remaining_time = datetime.strptime(race_time, fmt) - datetime.strptime(current_time, fmt)
    return remaining_time


def get_current_drivers_list():
    url = "https://ergast.com/api/f1/current/drivers.json"
    r = requests.get(url)
    data = r.json()
    drivers_list = data['MRData']['DriverTable']['Drivers']
    return drivers_list


# Wyświetlenie na ekran wyniku zadanych funkcji
print(get_current_date_utc())
print(get_current_time_utc())
print(get_current_races_list())
print(get_race_remaining_time_today())
print(get_current_drivers_list())