from datetime import datetime
import conf
import json


def date_time_parts(timestamp):
    dt = datetime.fromtimestamp(timestamp)
    return str(dt.year), str(dt.month), str(dt.day), str(dt.hour)


def format_ts(ts):
    dt = datetime.fromtimestamp(ts)
    # timestamps in the bgfs are integers (in seconds)
    # so we have to add the microseconds part
    return "{}.000000+00:00".format(dt.isoformat(sep=' '))
    
    
def trip_output_fields(trip):
    return {
        'started_at': format_ts(trip['start_time']), 
        'ended_at': format_ts(trip['end_time']), 
        'duration': trip['end_time'] - trip['start_time'], 
        'start_station_id': trip['start_station']['station_id'], 
        'start_station_name': trip['start_station']['name'], 
        'start_station_description': trip['start_station']['description'], 
        'start_station_latitude': trip['start_station']['lat'], 
        'start_station_longitude': trip['start_station']['lon'], 
        'end_station_id': trip['end_station']['station_id'], 
        'end_station_name': trip['end_station']['name'], 
        'end_station_description':trip['end_station']['description'], 
        'end_station_latitude': trip['end_station']['lat'],
        'end_station_longitude': trip['end_station']['lon'],
    }


CSV_HEADER = "started_at,ended_at,duration,start_station_id,start_station_name,start_station_description,start_station_latitude,start_station_longitude,end_station_id,end_station_name,end_station_description,end_station_latitude,end_station_longitude\n"


def csv_line(fields):
    return f"{fields['started_at']},{fields['ended_at']},{fields['duration']}," \
        f"{fields['start_station_id']},{fields['start_station_name']},{fields['start_station_description']},{fields['start_station_latitude']},{fields['start_station_longitude']}," \
        f"{fields['end_station_id']},{fields['end_station_name']},{fields['end_station_description']},{fields['end_station_latitude']},{fields['end_station_longitude']}\n"


def dump_csv(csv_file, trips_outputables):
    with open(csv_file, "w") as f_csv:
        f_csv.write(CSV_HEADER)
        for fields in trips_outputables:
            f_csv.write(csv_line(fields))


def dump_json(json_file, trips_outputables):
    with open(json_file, "w") as f_json:
        f_json.write(json.dumps(trips_outputables))
            

def is_trip_whole(trip):
    return 'start_station' in trip and trip['start_station']

    
def dump_whole_trips(next_dump_time, trips):
    trips_outputables = [trip_output_fields(trip) for trip in trips if is_trip_whole(trip)]
    
    year, month, day, hour = date_time_parts(next_dump_time - 1)
    dest = conf.DEST_PATH / "trips" / year / month / day
    dest.mkdir(parents=True, exist_ok=True)
    csv_file = dest / f"{hour}.csv"
    dump_csv(csv_file, trips_outputables)
    json_file = dest / f"{hour}.json"
    dump_json(json_file, trips_outputables)
    

