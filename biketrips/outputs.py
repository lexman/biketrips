from datetime import datetime
import conf


def date_time_parts(timestamp):
    dt = datetime.fromtimestamp(timestamp)
    return str(dt.year), str(dt.month), str(dt.day), str(dt.hour)
    
    
def trip_output_fields(trip):
    return {
        'started_at': trip['start_time'], 
        'ended_at': trip['end_time'], 
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


def csv_line(trip):
	fields = trip_output_fields(trip)
	return f"{fields['started_at']},"


def is_trip_whole(trip):
	return 'start_station' in trip and trip['start_station']

    
def dump_whole_trips(next_dump_time, trips):
    year,month,day,hour = date_time_parts(next_dump_time - 1)
    dest = conf.DEST_PATH / "trips" / year / month / day
    dest.mkdir(parents=True, exist_ok=True)
    csv_file = dest / f"{hour}.csv"
    with open(csv_file, "w") as f:
        for trip in trips:
            if is_trip_whole(trip):
                print(trip)
                f.write(csv_line(trip))
                f.write("\n")
