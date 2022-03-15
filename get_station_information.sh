echo $(date +"%Y-%m-%d %H:%M:%S")
FREE_BIKES_URL=https://eu.ftp.opendatasoft.com/star/gbfs/free_bike_status.json
REFRESH_FREQUENCY=60
mkdir -p free_bikes_history
while true
do
	curl $FREE_BIKES_URL > free_bikes_history/free_bike_status-$(date +"%Y-%m-%d_%H-%M-%S").json
	# Getting data is instant !
	sleep $REFRESH_FREQUENCY
done 
