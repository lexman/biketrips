import conf
from urllib.request import urlopen
from outputs import dump_csv, dump_json, date_time_parts, trip_output_fields
from gbfs import read_enabled_free_bikes, iter_free_bikes, iter_free_bikes_forever, read_stations
from trips import trips_iterator, haversine
import math


def dump_time(timestamp):
    return math.ceil(timestamp / conf.BATCH_COLLECT_DURATION ) * conf.BATCH_COLLECT_DURATION


def trip_batches(trips):
    complete_trips = []
    next_dump_time = None
    for trip in trips:
        if next_dump_time is None:
            next_dump_time = dump_time(trip['end_time'])
        while trip['end_time'] > next_dump_time:
            yield next_dump_time, complete_trips
            complete_trips = []
            next_dump_time += conf.BATCH_COLLECT_DURATION
        complete_trips.append(trip)
        
        
def is_trip_whole(trip):
    return 'start_station' in trip and trip['start_station']
    

def main():
    free_bikes_iterator = iter_free_bikes_forever(conf.HISTORY_PATH)
    response = urlopen(conf.STATION_INFROMATION_URL)
    stations = read_stations(response.read())
    
    it_trips = trips_iterator(free_bikes_iterator, stations)
    for ts, batch in trip_batches(it_trips):
        year, month, day, hour = date_time_parts(ts - 1)
        dest = conf.DEST_PATH / "trips" / year / month / day / str(ts)
        dest.mkdir(parents=True, exist_ok=True)
        
        trips_outputables = [trip_output_fields(trip) for trip in batch if is_trip_whole(trip)]
        dump_csv(dest / f"{hour}.csv", trips_outputables)
        dump_json(dest / f"{hour}.json", trips_outputables)
    
        print("Dumping a batch of {} trips in {}".format(len(trips_outputables), dest))
    # There are still trips before next hour waiting to be dumpe

if __name__ == "__main__":
    main()


