import conf
from glob import glob
from pathlib import Path
import json
import math


def read_enabled_free_bikes(filename):
    with open(filename) as f:
        try:
            obj = json.load(f)
            bikes = obj["data"]["bikes"]
            free_bikes = {
                bike["bike_id"]: bike for bike in bikes if bike["is_disabled"] == 0
            }
            return free_bikes
        except Exception as e:
            print(f"File {filename} the is not well formated. Ignoring...")
            print(e)


def get_next_free_bikes(history_path):
    free_bikes_hist = history_path.glob("*/free_bike_status.json")
    n = sorted(free_bikes_hist)[0]
    return read_enabled_free_bikes(n)


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
        lat = station["lat"]
        lon = station["lon"]
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


def haversine(lat1, lon1, lat2, lon2):
    radius_m = 6378137
    dlat = math.sin(math.radians(lat2 - lat1) * 0.5)
    dlon = math.sin(math.radians(lon2 - lon1) * 0.5)
    lat1 = math.cos(math.radians(lat1))
    lat2 = math.cos(math.radians(lat2))

    a = dlat ** 2 + lat1 * lat2 * dlon ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = radius_m * c

    return d


def find_nearest_station(bike_lon, _bike_lat, stations):
    nearest = None
    dist = None
    for st in stations.values():
        if nearest is None:
            nearest = st
            dist = haversine(bike_lon, _bike_lat, st['lon'], st['lat'])
        else:
            cur_dist = haversine(bike_lon, _bike_lat, st['lon'], st['lat'])
            if cur_dist <= dist:
                nearest = st
                dist = cur_dist
    return nearest


def batch_find_start(start_trip_bikes_ids, free_bikes, stations):
    for bike_id in start_trip_bikes_ids:
        nearest = find_nearest_station_id(
            free_bikes[bike_id].lat, free_bikes[bike_id].lon, stations
        )
        yield (
            bike_id,
            nearest,
        )


def apply_change(ongoing_trips, free_bikes):
    free_bikes_ids = ongoing_trips.bike_ids
    next_free_bikes_ids = {bike["bike_id"] for bike in free_bikes}
    start_trip_bikes_ids = next_free_bikes_ids - free_bikes_ids
    end_trip_bikes_ids = free_bikes_ids - next_free_bikes_ids
    new_trips = find_start(start_trip_bikes_ids, free_bikes, stations)


def main_loop(stations):
    free_bikes_ids = ongoing_trips.bike_ids
    while True:
        next_free_bikes = get_next_free_bikes()
        next_free_bikes_ids = {bike["bike_id"] for bike in next_free_bikes}
        start_trip_bikes_ids = next_free_bikes_ids - free_bikes_ids
        end_trip_bikes_ids = free_bikes_ids - next_free_bikes_ids
        new_trips = find_start(start_trip_bikes_ids, free_bikes, stations)
        free_bikes_ids = next_free_bikes_ids


def main():
    history_files = get_hist_files()
    free_bikes = history_files.pop()
    state = s
    ongoing_trips = state.ongoing_trips
    finished_trips = apply_change(ongoing_trips, free_bikes)


if __name__ == "__main__":
    stations_st = urlopen(conf.STATION_INFROMATION_URL).read()
    stations = list(iter_stations(stations_st))
    pass
    # main()

get_next_free_bikes(Path(conf.HISTORY_PATH))
