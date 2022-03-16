import conf
from urllib.request import urlopen
from outputs import dump_whole_trips
from gbfs import read_enabled_free_bikes, iter_free_bikes, iter_free_bikes_forever, read_stations
from trips import trips_iterator, haversine
import math


    

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
     

def debug_bike(free_bikes_iterator, bike_id):
    for next_free_bikes, updated in free_bikes_iterator:
        if bike_id in next_free_bikes:
            # print(next_free_bikes[bike_id])
            print("{},{}".format(next_free_bikes[bike_id]['lon'], next_free_bikes[bike_id]['lat']))
    

def next_hour(timestamp):
    return math.ceil(timestamp / 3600) * 3600



def trip_1h_batches(it_trips):
    complete_trips = []
    next_dump_time = None
    for trip in it_trips:
        debug_trip(trip)
        if next_dump_time is None:
            next_dump_time = next_hour(trip['end_time'])
        if trip['end_time'] > next_dump_time:
            yield next_dump_time, complete_trips
            complete_trips = []
            next_dump_time += 3600
        if trip['end_time'] <= next_dump_time:
            complete_trips.append(trip)
    
def main():
    free_bikes_iterator = iter_free_bikes(conf.HISTORY_PATH)
    response = urlopen(conf.STATION_INFROMATION_URL)
    stations = read_stations(response.read())
    
    it_trips = trips_iterator(free_bikes_iterator, stations)
    for ts, batch in trip_1h_batches(it_trips):
         dump_whole_trips(ts, batch)
    return
    

if __name__ == "__main__":
    main()


