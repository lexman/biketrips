import conf
from glob import glob
from pathlib import Path
import json
import math
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


def get_next_free_bikes(history_path):
    free_bikes_hist = history_path.glob("*/free_bike_status.json")
    next_file = sorted(free_bikes_hist)[0]
    return read_enabled_free_bikes(next_file)



def iter_free_bikes(history_path):
    """ Convention : files are added in time order
    ie : a previous file can't be added in a middle of a sequence, only in the end
     """

    free_bikes_hist = history_path.glob("*/free_bike_status.json")
    for next_file in sorted(free_bikes_hist):
        yield read_enabled_free_bikes(next_file)

    
def iter_free_bikes_forever(history_path):
    """ Convention : files are added in time order
    ie : a previous file can't be added in a middle of a sequence, only in the end
     """
    while True:
        yield from iter_free_bikes(history_path)
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
    return nearest, dist


def new_trips(start_time, start_trip_bikes_ids, free_bikes, stations):
    result = {}
    for bike_id in start_trip_bikes_ids:
        nearest, dist = find_nearest_station_id(
            free_bikes[bike_id].lat, free_bikes[bike_id].lon, stations
        )
        if dist > 200:
            nearest = None
        result[bike_id] = {
            'bike_id' : bike_id,
            'start_station' : nearest,
            'start_time' : start_time,
        }
    return result
    

def bike_ids(bikes):
    return {bike["bike_id"] for bike in bikes}


def bikes_from_ids(bike_ids, bikes):
    return {bike_id : bikes["bike_id"] for bike_id in bike_ids}
    

def complete_trips(updated, bike_ids, trips, bikes, stations):
    """ BEWARE : trips are mutated
    Remove the trips according to the bike_ids from the trips
    Returns the removed trips with an end_time and end_station
    """
    result = []
    for bike_id in bike_ids:
        trip = trips.pop(bike_id)
        trip['end_time'] = updated
        bike = bikes[bike_id]
        trip['end_station'] = find_nearest_station(bike['lon'], bike['lat'], stations)
        result.append(trip)
    return result

    
def trips_iterator(free_bikes_iterator, stations):
    free_bikes, updated = next(free_bikes_iterator)
    ongoing_trips_bike_ids = bike_ids(free_bikes)
    ongoing_trips = new_trips(updated, ongoing_trips_bike_ids, free_bikes, {})
    
    for next_free_bikes, updated in free_bikes_iterator:
        next_free_bikes_ids = bike_ids(next_free_bikes)
        
        end_trip_bikes_ids = free_bikes_ids - next_free_bikes_ids
        for trip in complete_trips(updated, end_trip_bikes_ids, ongoing_trips, bikes, stations):
            yield trip

        start_trip_bikes_ids = next_free_bikes_ids - free_bikes_ids
        new_trips = new_trips(start_trip_bikes_ids, free_bikes, stations)
        ongoing_trips.update(new_trips)
        free_bikes_ids = next_free_bikes_ids



def main_loop(stations):
    free_bikes, updated = get_next_free_bikes()
    ongoing_trips = new_trips(updated, bike_ids(free_bikes), free_bikes, {})
    
    while True:
        next_free_bikes, updated = get_next_free_bikes()
        next_free_bikes_ids = bike_ids(next_free_bikes)
        
        end_trip_bikes_ids = free_bikes_ids - next_free_bikes_ids
        completed_trips = complete_trips(updated, end_trip_bikes_ids, ongoing_trips, bikes, stations)

        start_trip_bikes_ids = next_free_bikes_ids - free_bikes_ids
        new_trips = new_trips(start_trip_bikes_ids, free_bikes, stations)
        free_bikes_ids = next_free_bikes_ids




if __name__ == "__main__":
    stations_st = urlopen(conf.STATION_INFROMATION_URL).read()
    stations = list(iter_stations(stations_st))
    pass
    # main()

