
FREE_BIKES_URL=https://gbfs.cogobikeshare.com/gbfs/en/free_bike_status.json
STATION_INFORMATION_URL=https://gbfs.cogobikeshare.com/gbfs/en/station_information.json
REFRESH_FREQUENCY=60
while true
do
	d=$(date +"%Y-%m-%d_%H-%M-%S")
	echo "At $d downloading :"
	echo "$FREE_BIKES_URL"
	mkdir -p "history/$d"
	curl $FREE_BIKES_URL > "history/$d/free_bike_status.json"
	echo "$STATION_INFORMATION_URL"
	curl $STATION_INFORMATION_URL > "history/$d/station_information.json"
	# Getting data is instant !
	sleep $REFRESH_FREQUENCY
done 
