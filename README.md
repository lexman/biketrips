# Bike trips

##  Purpose
This tools computes all bike trips from a GBFS provider, and export the list of trips every hours in CSV and JSON, available 
online at http://localhost:8000/trips/{year}/{month}/{day}/{hour}.csv and http://localhost:8000/trips/{year}/{month}/{day}/{hour}.json.
EG : http://localhost:8000/trips/2022/3/15/22.csv

## Install and run

### Requirements
This tools runs on Linux with Python 3. For example Ubuntu 2020.4. ``python3`` must be available from command line.


### Install
Clone the project from git or unzip the archive.

### Configure the settings

The program is configured to use GBFS from XXX. You can plug it to any GBFS feeds that meets both requirements :
* GBFS version 1.X
* GBFS provides both optionnal __station_information.json__ AND __free_bike_status.json__ urls

Edit file collect_history.sh to set the urls from the GBSF service :
FREE_BIKES_URL=
STATION_INFORMATION_URL=

You can also configure the polling frequency of free bike availability : REFRESH_FREQUENCY=

Edit the file biketrips/conf.py to set the STATION_INFROMATION_URL from the GBFS service


### Run
Open a new terminal and go to the project directory. Then launch run.sh :

. ./run.sh

This program runs the 3 components :
* the http server that exposes the csv and json files to download
* the downloader that polls the status of the bike network (logs in ``logs/polling.log``)
* the main program that computes the trips and export them 


To stop completely the program, you'll have to **close the terminal**.



## Test the core
If you don't want to wait one hour before you see you first batch of trips, you can make a simulation
Download the sample data, unzip it in sample and run the core

rm -rf history
cp -r sample history
python3 biketrips/main.py 

