import conf
from glob import glob
from pathlib import Path
import json


def read_enabled_free_bikes(filename):
    with open(filename) as f:
        try:
            obj = json.load(f)
            bikes = obj['data']['bikes']
            free_bikes = {bike['bike_id'] : bike for bike in bikes if bike['is_disabled'] == 0}
            return free_bikes
        except Exception as e:
            print(f"File {filename} the is not well formated. Ignoring...")
            print(e)



def get_next_free_bikes(history_path):
    free_bikes_hist = history_path.glob('*/free_bike_status.json')
    n = sorted(free_bikes_hist)[0]
    return read_enabled_free_bikes(n)
    
