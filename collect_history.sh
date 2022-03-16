#! /bin/bash

FREE_BIKES_URL=https://gbfs.cogobikeshare.com/gbfs/en/free_bike_status.json
STATION_INFORMATION_URL=https://gbfs.cogobikeshare.com/gbfs/en/station_information.json
REFRESH_FREQUENCY=60
HISTORY_DIR=history
while true
do
	d=$(date +"%Y-%m-%d_%H-%M-%S")
	echo "At $d downloading :"
	echo "$FREE_BIKES_URL"
	mkdir -p "$HISTORY_DIR/$d"
	curl $FREE_BIKES_URL > "$HISTORY_DIR/$d/free_bike_status.json"
	echo "$STATION_INFORMATION_URL"
	curl $STATION_INFORMATION_URL > "$HISTORY_DIR/$d/station_information.json"
	sleep $REFRESH_FREQUENCY # 
done 
