import conf
from glob import glob
from pathlib import Path
import json
import math
from urllib.request import urlopen
from time import sleep
import os
from outputs import dump_whole_trips



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


def find_nearest_station(bike_lon,_bike_lat, stations):
    nearest = None
    min_dist = None
    for st in stations.values():
        if nearest is None:
            nearest = st
            min_dist = haversine(bike_lon, _bike_lat, st['lon'], st['lat'])
        else:
            cur_dist = haversine(bike_lon, _bike_lat, st['lon'], st['lat'])
            if cur_dist <= min_dist:
                nearest = st
                min_dist = cur_dist
    return nearest, min_dist

    
def create_trips(start_time, bikes, all_stations):
    result = {}
    for bike in bikes.values():
        nearest, dist = find_nearest_station(
            bike['lon'], bike['lat'], all_stations
        )
        result[bike['bike_id']] = {
            'bike_id' : bike['bike_id'],
            'start_lon' : bike['lon'],
            'start_lat' : bike['lat'],
            'start_station' : nearest,
            'start_time' : start_time,
        }
    return result
    
    
def bike_ids(bikes):
    return {bike_id for bike_id in bikes}


def bikes_from_ids(bikes, bike_ids):
    return {bike_id : bikes[bike_id] for bike_id in bike_ids}
    

def complete_trips(trips, end_time, end_bikes, stations):
    """ BEWARE : trips are mutated
    Remove the trips according to the bike_ids from the trips
    Returns the removed trips with an end_time and end_station
    """
    result = []
    for bike in end_bikes.values():
        trip = trips.pop(bike['bike_id'])
        assert(trip['bike_id'] == bike['bike_id'])
        trip['end_time'] = end_time
        trip['end_lon'] = bike['lon']
        trip['end_lat'] = bike['lat']
        nearest, dist = find_nearest_station(bike['lon'], bike['lat'], stations)
        trip['end_station'] = nearest
        result.append(trip)
    return result

    
def trips_iterator(free_bikes_iterator, stations):
    free_bikes, updated = next(free_bikes_iterator)
    ongoing_trips_bike_ids = bike_ids(free_bikes)
    ongoing_trips = create_trips(updated, free_bikes, {})
    
    for next_free_bikes, updated in free_bikes_iterator:
        next_free_bikes_ids = bike_ids(next_free_bikes)
        
        end_trip_bikes_ids = ongoing_trips_bike_ids - next_free_bikes_ids
        end_trip_bikes = bikes_from_ids(free_bikes, end_trip_bikes_ids)
        for trip in complete_trips(ongoing_trips, updated, end_trip_bikes, stations):
            yield trip

        start_trip_bikes_ids = next_free_bikes_ids - ongoing_trips_bike_ids
        start_trip_bikes = bikes_from_ids(next_free_bikes, start_trip_bikes_ids)
        new_trips = create_trips(updated, start_trip_bikes, stations)
        ongoing_trips.update(new_trips)
        ongoing_trips_bike_ids = next_free_bikes_ids
        free_bikes = next_free_bikes


def debug_trip(trip):

    dist = haversine(trip['start_lon'], trip['start_lat'], trip['end_lon'], trip['end_lat'])
    duration = math.floor((trip['end_time']- trip['start_time']) / 60)
    delta_start = None
    if trip['start_station']:
        delta_start = haversine(trip['start_lon'], trip['start_lat'], trip['start_station']['lon'], trip['start_station']['lat'])
    delta_end = None
    if trip['end_station']:
        delta_end = haversine(trip['end_lon'], trip['end_lat'], trip['end_station']['lon'], trip['end_station']['lat'])   
    #if delta_start and delta_start > 0:
    if dist > 30:
        print(trip)
        print("Dist : {} - Duration : {} - delta_start : {} - delta_end : {}".format(dist, duration, delta_start, delta_end))
        

def next_hour(timestamp):
    return math.ceil(timestamp / 3600) * 3600


def debug_bike(free_bikes_iterator, bike_id):
    for next_free_bikes, updated in free_bikes_iterator:
        if bike_id in next_free_bikes:
            print(next_free_bikes[bike_id])
    
    
    
def main():
    free_bikes_iterator = iter_free_bikes(conf.HISTORY_PATH)
    debug_bike(free_bikes_iterator, "f1415ecccec5fe01d0cb840eeb771f22")
    end
    response = urlopen(conf.STATION_INFROMATION_URL)
    stations = read_stations(response.read())
    complete_trips = []
    next_dump_time = None
    for trip in trips_iterator(free_bikes_iterator, stations):
        debug_trip(trip)
        if next_dump_time is None:
            next_dump_time = next_hour(trip['end_time'])
        if trip['end_time'] > next_dump_time:
            dump_whole_trips(next_dump_time, complete_trips)
            print( "{} - {}".format(trip['end_time'], next_dump_time))
            complete_trips = []
            next_dump_time += 3600
        complete_trips.append(trip)
        debug_trip(trip)


if __name__ == "__main__":
    main()


