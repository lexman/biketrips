import math


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


def bike_ids(bikes):
    return {bike_id for bike_id in bikes}


def bikes_from_ids(bikes, bike_ids):
    return {bike_id : bikes[bike_id] for bike_id in bike_ids}


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
        removed_trips = complete_trips(ongoing_trips, updated, end_trip_bikes, stations)
        assert len(removed_trips) == len(end_trip_bikes)
        for trip in removed_trips:
            yield trip

        start_trip_bikes_ids = next_free_bikes_ids - ongoing_trips_bike_ids
        start_trip_bikes = bikes_from_ids(next_free_bikes, start_trip_bikes_ids)
        new_trips = create_trips(updated, start_trip_bikes, stations)
        ongoing_trips.update(new_trips)
        ongoing_trips_bike_ids = next_free_bikes_ids
        free_bikes = next_free_bikes
