from pathlib import Path


# Be sure to have path relative to this file
HISTORY_PATH = Path(__file__).parent / Path("../history_bak/")
DEST_PATH = Path(__file__).parent / Path("../www/")

STATION_INFROMATION_URL = "https://gbfs.cogobikeshare.com/gbfs/en/station_information.json"
