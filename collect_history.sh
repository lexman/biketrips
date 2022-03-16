#! /bin/bash

FREE_BIKES_URL=https://gbfs.cogobikeshare.com/gbfs/en/free_bike_status.json
STATION_INFORMATION_URL=https://gbfs.cogobikeshare.com/gbfs/en/station_information.json
REFRESH_FREQUENCY=59
HISTORY_DIR=history
HISTORY_BACKUP_DIR=history_backup

mkdir -p tmp
while true
do
	d=$(date +"%Y-%m-%d_%H-%M-%S")
	echo "At $d downloading :"
	echo "$FREE_BIKES_URL"
	mkdir -p "$HISTORY_DIR/$d"
	mkdir -p "$HISTORY_BACKUP_DIR/$d"
	curl $FREE_BIKES_URL > tmp/free_bike_status.json
	cp tmp/free_bike_status.json "$HISTORY_BACKUP_DIR/$d/free_bike_status.json"
	mv tmp/free_bike_status.json "$HISTORY_DIR/$d/free_bike_status.json"
	sleep $REFRESH_FREQUENCY # 
done 
