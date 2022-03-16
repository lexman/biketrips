import json
from time import sleep



def read_enabled_free_bikes(filename):
    with open(filename) as f:
        try:
            obj = json.load(f)
            bikes = obj["data"]["bikes"]
            free_bikes = {
                bike["bike_id"]: bike for bike in bikes if bike["is_disabled"] == 0
            }
            return free_bikes, obj['last_updated']
        except Exception as e:
            print(f"File {filename} the is not well formated. Ignoring...")
            print(e)



def iter_free_bikes(history_path, delete_files=False):
    free_bikes_hist = history_path.glob("*/free_bike_status.json")
    for next_file in sorted(free_bikes_hist):
         free_bikes = read_enabled_free_bikes(next_file)
         yield free_bikes
         if delete_files:
             print(f"Deleteing {next_file}")
             next_file.unlink()
    
def iter_free_bikes_forever(history_path):
    """ Convention : files are added in time order
    ie : a previous file can't be added in a middle of a sequence, only in the end
     """
    while True:
        yield from iter_free_bikes(history_path, delete_files=True)
        print(f"Waiting for new free_bikes files in {history_path}")
        sleep(1)


def optional_field(dico, fieldname):
    if fieldname in dico:
        return dico[fieldname]
    else:
        return ""


def read_stations(stations_st):
    data_json = json.loads(stations_st)
    assert "data" in data_json and "stations" in data_json["data"]
    stations = data_json["data"]["stations"]
    result = {}
    for station in stations:
        station_id = station["station_id"]
        lon = station["lon"]
        lat = station["lat"]
        name = optional_field(station, "name")
        description = optional_field(station, "address")
        result[station_id] = {
            "station_id": station_id,
            "lon": lon,
            "lat": lat,
            "name": name,
            "description": description,
        }
    return result
