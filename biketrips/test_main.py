import unittest
import main
from pathlib import Path
import outputs
import gbfs
import trips


class TestFeed(unittest.TestCase):
    exemple_free_bikes = {
        "902606c04933d5c85a8a4fcfffd222c4": {
            "is_reserved": 0,
            "bike_id": "902606c04933d5c85a8a4fcfffd222c4",
            "type": "electric_bike",
            "lat": 39.9690315,
            "name": "902606c04933d5c85a8a4fcfffd222c4",
            "is_disabled": 0,
            "lon": -82.999674,
            "rental_uris": {
                "android": "https://lyft.com/lastmile_qr_scan",
                "ios": "https://lyft.com/lastmile_qr_scan",
            },
        },
        "dd2f4729320a56162dd760bb6edd82cd": {
            "is_reserved": 0,
            "bike_id": "dd2f4729320a56162dd760bb6edd82cd",
            "type": "electric_bike",
            "lat": 39.9690745,
            "name": "dd2f4729320a56162dd760bb6edd82cd",
            "is_disabled": 0,
            "lon": -83.00050666666667,
            "rental_uris": {
                "android": "https://lyft.com/lastmile_qr_scan",
                "ios": "https://lyft.com/lastmile_qr_scan",
            },
        },
        "ccfb9b0a95f6445fa6eeb293a876a168": {
            "is_reserved": 0,
            "bike_id": "ccfb9b0a95f6445fa6eeb293a876a168",
            "type": "electric_bike",
            "lat": 39.9873685,
            "name": "ccfb9b0a95f6445fa6eeb293a876a168",
            "is_disabled": 0,
            "lon": -83.02300433333333,
            "rental_uris": {
                "android": "https://lyft.com/lastmile_qr_scan",
                "ios": "https://lyft.com/lastmile_qr_scan",
            },
        },
        "0e9f170ac1207ac4695066c4bd320c31": {
            "is_reserved": 0,
            "bike_id": "0e9f170ac1207ac4695066c4bd320c31",
            "type": "electric_bike",
            "lat": 39.967627666666665,
            "name": "0e9f170ac1207ac4695066c4bd320c31",
            "is_disabled": 0,
            "lon": -83.0072515,
            "rental_uris": {
                "android": "https://lyft.com/lastmile_qr_scan",
                "ios": "https://lyft.com/lastmile_qr_scan",
            },
        },
        "a0d2923aeabfa74fa7efdbb81af6d7b5": {
            "is_reserved": 0,
            "bike_id": "a0d2923aeabfa74fa7efdbb81af6d7b5",
            "type": "electric_bike",
            "lat": 39.9575575,
            "name": "a0d2923aeabfa74fa7efdbb81af6d7b5",
            "is_disabled": 0,
            "lon": -83.00071033333333,
            "rental_uris": {
                "android": "https://lyft.com/lastmile_qr_scan",
                "ios": "https://lyft.com/lastmile_qr_scan",
            },
        },
        "efe948758cec1ce3d789c2a536364d47": {
            "is_reserved": 0,
            "bike_id": "efe948758cec1ce3d789c2a536364d47",
            "type": "electric_bike",
            "lat": 39.95272416666667,
            "name": "efe948758cec1ce3d789c2a536364d47",
            "is_disabled": 0,
            "lon": -82.97675433333333,
            "rental_uris": {
                "android": "https://lyft.com/lastmile_qr_scan",
                "ios": "https://lyft.com/lastmile_qr_scan",
            },
        },
        "4b343d62b5d2b6c8ba30ffcc9ca9f583": {
            "is_reserved": 0,
            "bike_id": "4b343d62b5d2b6c8ba30ffcc9ca9f583",
            "type": "electric_bike",
            "lat": 39.9990445,
            "name": "4b343d62b5d2b6c8ba30ffcc9ca9f583",
            "is_disabled": 0,
            "lon": -83.01734666666667,
            "rental_uris": {
                "android": "https://lyft.com/lastmile_qr_scan",
                "ios": "https://lyft.com/lastmile_qr_scan",
            },
        },
        "57655756aea1090bedd9539315c4c415": {
            "is_reserved": 0,
            "bike_id": "57655756aea1090bedd9539315c4c415",
            "type": "electric_bike",
            "lat": 39.9774015,
            "name": "57655756aea1090bedd9539315c4c415",
            "is_disabled": 0,
            "lon": -83.01164883333334,
            "rental_uris": {
                "android": "https://lyft.com/lastmile_qr_scan",
                "ios": "https://lyft.com/lastmile_qr_scan",
            },
        },
        "e0a9c2aba70c2b9b66134b6f9da46b87": {
            "is_reserved": 0,
            "bike_id": "e0a9c2aba70c2b9b66134b6f9da46b87",
            "type": "electric_bike",
            "lat": 39.99114216666667,
            "name": "e0a9c2aba70c2b9b66134b6f9da46b87",
            "is_disabled": 0,
            "lon": -83.006453,
            "rental_uris": {
                "android": "https://lyft.com/lastmile_qr_scan",
                "ios": "https://lyft.com/lastmile_qr_scan",
            },
        },
        "7939d8e3f69110eeb4c712dcbc5a2db4": {
            "is_reserved": 0,
            "bike_id": "7939d8e3f69110eeb4c712dcbc5a2db4",
            "type": "electric_bike",
            "lat": 39.98730466666667,
            "name": "7939d8e3f69110eeb4c712dcbc5a2db4",
            "is_disabled": 0,
            "lon": -83.02291116666666,
            "rental_uris": {
                "android": "https://lyft.com/lastmile_qr_scan",
                "ios": "https://lyft.com/lastmile_qr_scan",
            },
        },
        "9d77c9b9158151845b63e3deee5ea67d": {
            "is_reserved": 0,
            "bike_id": "9d77c9b9158151845b63e3deee5ea67d",
            "type": "electric_bike",
            "lat": 39.96899166666667,
            "name": "9d77c9b9158151845b63e3deee5ea67d",
            "is_disabled": 0,
            "lon": -82.999581,
            "rental_uris": {
                "android": "https://lyft.com/lastmile_qr_scan",
                "ios": "https://lyft.com/lastmile_qr_scan",
            },
        },
        "e4613309780073a7fbd99ca95b4d0a4e": {
            "is_reserved": 0,
            "bike_id": "e4613309780073a7fbd99ca95b4d0a4e",
            "type": "electric_bike",
            "lat": 39.949966333333336,
            "name": "e4613309780073a7fbd99ca95b4d0a4e",
            "is_disabled": 0,
            "lon": -82.9568525,
            "rental_uris": {
                "android": "https://lyft.com/lastmile_qr_scan",
                "ios": "https://lyft.com/lastmile_qr_scan",
            },
        },
        "49b79c78a274b6b7391affc07bb94e3a": {
            "is_reserved": 0,
            "bike_id": "49b79c78a274b6b7391affc07bb94e3a",
            "type": "electric_bike",
            "lat": 40.00916183333333,
            "name": "49b79c78a274b6b7391affc07bb94e3a",
            "is_disabled": 0,
            "lon": -83.01368066666667,
            "rental_uris": {
                "android": "https://lyft.com/lastmile_qr_scan",
                "ios": "https://lyft.com/lastmile_qr_scan",
            },
        },
        "7b73b3115d38886be8943543a19114f3": {
            "is_reserved": 0,
            "bike_id": "7b73b3115d38886be8943543a19114f3",
            "type": "electric_bike",
            "lat": 39.961820333333335,
            "name": "7b73b3115d38886be8943543a19114f3",
            "is_disabled": 0,
            "lon": -82.96551716666667,
            "rental_uris": {
                "android": "https://lyft.com/lastmile_qr_scan",
                "ios": "https://lyft.com/lastmile_qr_scan",
            },
        },
    }

    example_stations = {
        "d63c5761-3168-11ea-a9c2-021785291289": {
            "station_id": "d63c5761-3168-11ea-a9c2-021785291289",
            "lon": -83.0083875,
            "lat": 40.001107,
            "name": "High St & 17th Ave",
            "description": "",
        },
        "d63bbed4-3168-11ea-a9c2-021785291289": {
            "station_id": "d63bbed4-3168-11ea-a9c2-021785291289",
            "lon": -83.001536,
            "lat": 39.965888,
            "name": "High St & Spring St",
            "description": "",
        },
        "d63bf2e6-3168-11ea-a9c2-021785291289": {
            "station_id": "d63bf2e6-3168-11ea-a9c2-021785291289",
            "lon": -82.9908445,
            "lat": 39.961557,
            "name": "Library - Main Branch",
            "description": "",
        },
        "d63b84f1-3168-11ea-a9c2-021785291289": {
            "station_id": "d63b84f1-3168-11ea-a9c2-021785291289",
            "lon": -82.998983,
            "lat": 39.9546,
            "name": "Dorrian Commons - Mound St",
            "description": "",
        },
        "d63d0344-3168-11ea-a9c2-021785291289": {
            "station_id": "d63d0344-3168-11ea-a9c2-021785291289",
            "lon": -83.039975,
            "lat": 39.9847325,
            "name": "Northwest Blvd & 3rd Ave",
            "description": "",
        },
        "d63be971-3168-11ea-a9c2-021785291289": {
            "station_id": "d63be971-3168-11ea-a9c2-021785291289",
            "lon": -82.990458,
            "lat": 39.9651575,
            "name": "Columbus College of Art & Design",
            "description": "",
        },
        "d63cfeb5-3168-11ea-a9c2-021785291289": {
            "station_id": "d63cfeb5-3168-11ea-a9c2-021785291289",
            "lon": -83.0087715,
            "lat": 39.964999,
            "name": "North Bank Park",
            "description": "",
        },
        "d63abbf5-3168-11ea-a9c2-021785291289": {
            "station_id": "d63abbf5-3168-11ea-a9c2-021785291289",
            "lon": -83.0032215,
            "lat": 39.955924,
            "name": "Bicentennial Park",
            "description": "",
        },
        "d63cf037-3168-11ea-a9c2-021785291289": {
            "station_id": "d63cf037-3168-11ea-a9c2-021785291289",
            "lon": -83.000232,
            "lat": 40.0146755,
            "name": "Summit St & Hudson St",
            "description": "",
        },
        "d63b9a40-3168-11ea-a9c2-021785291289": {
            "station_id": "d63b9a40-3168-11ea-a9c2-021785291289",
            "lon": -82.998107,
            "lat": 39.957608,
            "name": "Columbus Commons - Rich St",
            "description": "",
        },
        "d63cf544-3168-11ea-a9c2-021785291289": {
            "station_id": "d63cf544-3168-11ea-a9c2-021785291289",
            "lon": -82.9617595,
            "lat": 39.9679915,
            "name": "Taylor Ave & Long St",
            "description": "",
        },
        "d63caf6c-3168-11ea-a9c2-021785291289": {
            "station_id": "d63caf6c-3168-11ea-a9c2-021785291289",
            "lon": -83.067873,
            "lat": 40.013509,
            "name": "Tremont Center at Tremont Rd",
            "description": "",
        },
        "d63cfa01-3168-11ea-a9c2-021785291289": {
            "station_id": "d63cfa01-3168-11ea-a9c2-021785291289",
            "lon": -82.953245,
            "lat": 39.963267,
            "name": "Franklin Park at Fairwood Ave",
            "description": "",
        },
        "d63b9ede-3168-11ea-a9c2-021785291289": {
            "station_id": "d63b9ede-3168-11ea-a9c2-021785291289",
            "lon": -82.995355,
            "lat": 39.949433,
            "name": "3rd St & Sycamore St",
            "description": "",
        },
        "d63bdf89-3168-11ea-a9c2-021785291289": {
            "station_id": "d63bdf89-3168-11ea-a9c2-021785291289",
            "lon": -83.004787,
            "lat": 39.982784,
            "name": "High St & 2nd Ave",
            "description": "",
        },
        "d63bd5ab-3168-11ea-a9c2-021785291289": {
            "station_id": "d63bd5ab-3168-11ea-a9c2-021785291289",
            "lon": -83.0115745,
            "lat": 39.9774165,
            "name": "Neil Ave & Buttles Ave",
            "description": "",
        },
        "d63cc1ae-3168-11ea-a9c2-021785291289": {
            "station_id": "d63cc1ae-3168-11ea-a9c2-021785291289",
            "lon": -83.0445105,
            "lat": 39.985158,
            "name": "Grandview Ave & 3rd Ave",
            "description": "",
        },
        "d63b7f96-3168-11ea-a9c2-021785291289": {
            "station_id": "d63b7f96-3168-11ea-a9c2-021785291289",
            "lon": -83.0090465,
            "lat": 39.945884,
            "name": "Scioto Audubon Center",
            "description": "",
        },
        "d63bf77f-3168-11ea-a9c2-021785291289": {
            "station_id": "d63bf77f-3168-11ea-a9c2-021785291289",
            "lon": -82.9868825,
            "lat": 39.9602635,
            "name": "Topiary Park - Town St",
            "description": "",
        },
        "d63bc7f7-3168-11ea-a9c2-021785291289": {
            "station_id": "d63bc7f7-3168-11ea-a9c2-021785291289",
            "lon": -83.0064855,
            "lat": 39.96116,
            "name": "COSI",
            "description": "",
        },
        "d63c727c-3168-11ea-a9c2-021785291289": {
            "station_id": "d63c727c-3168-11ea-a9c2-021785291289",
            "lon": -83.020464,
            "lat": 40.006583,
            "name": "Lane Ave at Olentangy Trail",
            "description": "",
        },
        "d63c6df7-3168-11ea-a9c2-021785291289": {
            "station_id": "d63c6df7-3168-11ea-a9c2-021785291289",
            "lon": -82.9894985,
            "lat": 39.9446015,
            "name": "Jaeger St & Whittier St",
            "description": "",
        },
        "d63c8a52-3168-11ea-a9c2-021785291289": {
            "station_id": "d63c8a52-3168-11ea-a9c2-021785291289",
            "lon": -82.914337,
            "lat": 40.037329,
            "name": "Easton Square Pl & Loyalty Circle",
            "description": "",
        },
        "d63ca61e-3168-11ea-a9c2-021785291289": {
            "station_id": "d63ca61e-3168-11ea-a9c2-021785291289",
            "lon": -82.9445055,
            "lat": 39.971343,
            "name": "Jeffrey Park on Clifton Ave",
            "description": "",
        },
        "9f00ab91-5b84-482d-af30-0fcf3d4a5d9f": {
            "station_id": "9f00ab91-5b84-482d-af30-0fcf3d4a5d9f",
            "lon": -82.9098325,
            "lat": 40.060836,
            "name": "Easton Transit Center",
            "description": "",
        },
        "d63ba7e5-3168-11ea-a9c2-021785291289": {
            "station_id": "d63ba7e5-3168-11ea-a9c2-021785291289",
            "lon": -83.002202,
            "lat": 39.971255,
            "name": "Convention Center",
            "description": "",
        },
        "d63cebb8-3168-11ea-a9c2-021785291289": {
            "station_id": "d63cebb8-3168-11ea-a9c2-021785291289",
            "lon": -83.013642,
            "lat": 40.022519,
            "name": "High St & Crestview Rd",
            "description": "",
        },
        "d63ce736-3168-11ea-a9c2-021785291289": {
            "station_id": "d63ce736-3168-11ea-a9c2-021785291289",
            "lon": -83.0110875,
            "lat": 40.014607,
            "name": "High St & Hudson St",
            "description": "",
        },
        "d63cb3fc-3168-11ea-a9c2-021785291289": {
            "station_id": "d63cb3fc-3168-11ea-a9c2-021785291289",
            "lon": -83.0516705,
            "lat": 40.0071635,
            "name": "Wellesley Dr & Lane Ave",
            "description": "",
        },
        "d63c9846-3168-11ea-a9c2-021785291289": {
            "station_id": "d63c9846-3168-11ea-a9c2-021785291289",
            "lon": -82.926169,
            "lat": 39.9569695,
            "name": "Grandon Ave & Main St",
            "description": "",
        },
        "dffd4a67-9fc5-4b0f-a3ee-48bc3ff40950": {
            "station_id": "dffd4a67-9fc5-4b0f-a3ee-48bc3ff40950",
            "lon": -83.0190521478653,
            "lat": 40.041221957165284,
            "name": "Library - Whetstone Branch",
            "description": "",
        },
        "d63c52c6-3168-11ea-a9c2-021785291289": {
            "station_id": "d63c52c6-3168-11ea-a9c2-021785291289",
            "lon": -83.0071245,
            "lat": 39.9947255,
            "name": "High St & 11th Ave",
            "description": "",
        },
        "d63bcc80-3168-11ea-a9c2-021785291289": {
            "station_id": "d63bcc80-3168-11ea-a9c2-021785291289",
            "lon": -83.0035705,
            "lat": 39.9721975,
            "name": "North Market",
            "description": "",
        },
        "d63cb89d-3168-11ea-a9c2-021785291289": {
            "station_id": "d63cb89d-3168-11ea-a9c2-021785291289",
            "lon": -83.0490005,
            "lat": 39.9967685,
            "name": "North Star Rd & Northwest Blvd",
            "description": "",
        },
        "d63acb22-3168-11ea-a9c2-021785291289": {
            "station_id": "d63acb22-3168-11ea-a9c2-021785291289",
            "lon": -83.0002435,
            "lat": 39.950149,
            "name": "Front St & Beck St",
            "description": "",
        },
        "d63cd99b-3168-11ea-a9c2-021785291289": {
            "station_id": "d63cd99b-3168-11ea-a9c2-021785291289",
            "lon": -83.009192,
            "lat": 40.0063975,
            "name": "High St & Lane Ave",
            "description": "",
        },
        "d63b8bd0-3168-11ea-a9c2-021785291289": {
            "station_id": "d63b8bd0-3168-11ea-a9c2-021785291289",
            "lon": -82.9950175,
            "lat": 39.941996,
            "name": "Schiller Park - Stewart Ave",
            "description": "",
        },
        "d63cde22-3168-11ea-a9c2-021785291289": {
            "station_id": "d63cde22-3168-11ea-a9c2-021785291289",
            "lon": -83.0011625,
            "lat": 40.001957,
            "name": "Summit St & 17th Ave",
            "description": "",
        },
        "ec36822c-f636-4cf6-88e4-f2afd565a02b": {
            "station_id": "ec36822c-f636-4cf6-88e4-f2afd565a02b",
            "lon": -83.0191557,
            "lat": 39.967324,
            "name": "Neiland and Nationwide",
            "description": "",
        },
        "d63c64f5-3168-11ea-a9c2-021785291289": {
            "station_id": "d63c64f5-3168-11ea-a9c2-021785291289",
            "lon": -83.016892,
            "lat": 39.984092,
            "name": "Michigan Ave & 3rd Ave",
            "description": "",
        },
        "d63bda4d-3168-11ea-a9c2-021785291289": {
            "station_id": "d63bda4d-3168-11ea-a9c2-021785291289",
            "lon": -83.0035065,
            "lat": 39.977479,
            "name": "High St & Warren",
            "description": "",
        },
        "d63caac7-3168-11ea-a9c2-021785291289": {
            "station_id": "d63caac7-3168-11ea-a9c2-021785291289",
            "lon": -83.0575055,
            "lat": 40.0189615,
            "name": "Northwest Blvd and Zollinger Rd",
            "description": "",
        },
        "d63c409d-3168-11ea-a9c2-021785291289": {
            "station_id": "d63c409d-3168-11ea-a9c2-021785291289",
            "lon": -82.998027,
            "lat": 39.980568,
            "name": "GO FITNESS IV (Italian Village) 4th/1st",
            "description": "",
        },
        "d63ce2a2-3168-11ea-a9c2-021785291289": {
            "station_id": "d63ce2a2-3168-11ea-a9c2-021785291289",
            "lon": -82.989416,
            "lat": 39.9859055,
            "name": "Cleveland Ave & 4th Ave",
            "description": "",
        },
        "d63c6069-3168-11ea-a9c2-021785291289": {
            "station_id": "d63c6069-3168-11ea-a9c2-021785291289",
            "lon": -83.013582,
            "lat": 39.9902415,
            "name": "Neil Ave & King Ave",
            "description": "",
        },
        "42f01987-2da2-4569-868e-887dd83da3a1": {
            "station_id": "42f01987-2da2-4569-868e-887dd83da3a1",
            "lon": -82.98337172716856,
            "lat": 39.94042266690196,
            "name": "Library - Parsons Branch",
            "description": "",
        },
        "d63d07de-3168-11ea-a9c2-021785291289": {
            "station_id": "d63d07de-3168-11ea-a9c2-021785291289",
            "lon": -83.0422135,
            "lat": 39.9935795,
            "name": "Northwest Blvd & Chambers Rd",
            "description": "",
        },
        "d63ba363-3168-11ea-a9c2-021785291289": {
            "station_id": "d63ba363-3168-11ea-a9c2-021785291289",
            "lon": -83.0040165,
            "lat": 39.969172,
            "name": "Nationwide Arena - Front St",
            "description": "",
        },
        "d63b90df-3168-11ea-a9c2-021785291289": {
            "station_id": "d63b90df-3168-11ea-a9c2-021785291289",
            "lon": -83.00851,
            "lat": 39.9680165,
            "name": "Neil Ave & Nationwide Blvd",
            "description": "",
        },
        "d63bfc16-3168-11ea-a9c2-021785291289": {
            "station_id": "d63bfc16-3168-11ea-a9c2-021785291289",
            "lon": -82.981344,
            "lat": 39.9632325,
            "name": "Parsons Ave & Oak St",
            "description": "",
        },
        "d63b958c-3168-11ea-a9c2-021785291289": {
            "station_id": "d63b958c-3168-11ea-a9c2-021785291289",
            "lon": -83.0003495,
            "lat": 39.9465955,
            "name": "Bank St & Frankfort St",
            "description": "",
        },
        "d63bb5aa-3168-11ea-a9c2-021785291289": {
            "station_id": "d63bb5aa-3168-11ea-a9c2-021785291289",
            "lon": -82.9900715,
            "lat": 39.9575095,
            "name": "Grant Ave & Main St",
            "description": "",
        },
        "d63ac3a4-3168-11ea-a9c2-021785291289": {
            "station_id": "d63ac3a4-3168-11ea-a9c2-021785291289",
            "lon": -83.004253,
            "lat": 39.962989,
            "name": "City Hall",
            "description": "",
        },
        "d63bc36a-3168-11ea-a9c2-021785291289": {
            "station_id": "d63bc36a-3168-11ea-a9c2-021785291289",
            "lon": -82.9986475,
            "lat": 39.963983,
            "name": "3rd St & Gay St",
            "description": "",
        },
        "d63c9cd3-3168-11ea-a9c2-021785291289": {
            "station_id": "d63c9cd3-3168-11ea-a9c2-021785291289",
            "lon": -82.936316,
            "lat": 39.9553655,
            "name": "Pleasant Ridge Ave & Mound St",
            "description": "",
        },
        "d63bee51-3168-11ea-a9c2-021785291289": {
            "station_id": "d63bee51-3168-11ea-a9c2-021785291289",
            "lon": -82.9871527,
            "lat": 39.964532,
            "name": "Columbus Museum of Art",
            "description": "",
        },
        "d63cbd1e-3168-11ea-a9c2-021785291289": {
            "station_id": "d63cbd1e-3168-11ea-a9c2-021785291289",
            "lon": -83.0617315,
            "lat": 39.9988165,
            "name": "Mallway Park at Arlington Ave",
            "description": "",
        },
        "d63d1a37-3168-11ea-a9c2-021785291289": {
            "station_id": "d63d1a37-3168-11ea-a9c2-021785291289",
            "lon": -82.9081665,
            "lat": 40.055071,
            "name": "Seward St & Worth Ave",
            "description": "",
        },
        "c6c6199c-32a4-4edf-a46a-967d713a4824": {
            "station_id": "c6c6199c-32a4-4edf-a46a-967d713a4824",
            "lon": -82.9682205,
            "lat": 40.0128495,
            "name": "Library - Linden Branch",
            "description": "",
        },
        "d63bb129-3168-11ea-a9c2-021785291289": {
            "station_id": "d63bb129-3168-11ea-a9c2-021785291289",
            "lon": -82.9790935,
            "lat": 39.951377,
            "name": "Livingston Park",
            "description": "",
        },
        "d63ccac5-3168-11ea-a9c2-021785291289": {
            "station_id": "d63ccac5-3168-11ea-a9c2-021785291289",
            "lon": -83.0258675,
            "lat": 39.9770195,
            "name": "Yard St & Burr Ave",
            "description": "",
        },
        "d63c4e3f-3168-11ea-a9c2-021785291289": {
            "station_id": "d63c4e3f-3168-11ea-a9c2-021785291289",
            "lon": -83.0058285,
            "lat": 39.9901425,
            "name": "High St & King Ave",
            "description": "",
        },
        "d63ccf5c-3168-11ea-a9c2-021785291289": {
            "station_id": "d63ccf5c-3168-11ea-a9c2-021785291289",
            "lon": -83.0326855,
            "lat": 39.97996,
            "name": "Northwest Blvd & 1st Ave",
            "description": "",
        },
        "d63bac86-3168-11ea-a9c2-021785291289": {
            "station_id": "d63bac86-3168-11ea-a9c2-021785291289",
            "lon": -83.001122,
            "lat": 39.962012,
            "name": "High St & Broad St",
            "description": "",
        },
        "97ff94a7-da2a-4500-989c-c25caa16fac9": {
            "station_id": "97ff94a7-da2a-4500-989c-c25caa16fac9",
            "lon": -82.98883236944674,
            "lat": 39.93589714085142,
            "name": "Moeller Park at Bruck St",
            "description": "",
        },
        "5d3f1dda-ec98-4749-a5a7-cc5048a851ef": {
            "station_id": "5d3f1dda-ec98-4749-a5a7-cc5048a851ef",
            "lon": -82.97900676727295,
            "lat": 39.97110065411914,
            "name": "King Arts Complex",
            "description": "",
        },
        "d63d15a9-3168-11ea-a9c2-021785291289": {
            "station_id": "d63d15a9-3168-11ea-a9c2-021785291289",
            "lon": -82.9116552,
            "lat": 40.0535477,
            "name": "Brighton Rose & Worth Ave",
            "description": "",
        },
        "d63c3c09-3168-11ea-a9c2-021785291289": {
            "station_id": "d63c3c09-3168-11ea-a9c2-021785291289",
            "lon": -82.9691835,
            "lat": 39.957748,
            "name": "Champion Ave & Main St",
            "description": "",
        },
        "d63c8f1d-3168-11ea-a9c2-021785291289": {
            "station_id": "d63c8f1d-3168-11ea-a9c2-021785291289",
            "lon": -82.910212,
            "lat": 40.0566725,
            "name": "Stelzer Rd & Morse Rd",
            "description": "",
        },
        "d63cd4d0-3168-11ea-a9c2-021785291289": {
            "station_id": "d63cd4d0-3168-11ea-a9c2-021785291289",
            "lon": -83.001959,
            "lat": 39.9590745,
            "name": "Front St & Town St",
            "description": "",
        },
        "d63c8022-3168-11ea-a9c2-021785291289": {
            "station_id": "d63c8022-3168-11ea-a9c2-021785291289",
            "lon": -82.9063305,
            "lat": 40.0445335,
            "name": "Easton Oval",
            "description": "",
        },
        "d63d1110-3168-11ea-a9c2-021785291289": {
            "station_id": "d63d1110-3168-11ea-a9c2-021785291289",
            "lon": -82.9152355,
            "lat": 40.0488005,
            "name": "Easton Square Pl & Townsfair Way",
            "description": "",
        },
        "d63c770b-3168-11ea-a9c2-021785291289": {
            "station_id": "d63c770b-3168-11ea-a9c2-021785291289",
            "lon": -82.987683,
            "lat": 39.9396375,
            "name": "Thurman Ave & Bruck St",
            "description": "",
        },
        "d63c857f-3168-11ea-a9c2-021785291289": {
            "station_id": "d63c857f-3168-11ea-a9c2-021785291289",
            "lon": -82.9104665,
            "lat": 40.047495,
            "name": "Stelzer & Easton Way",
            "description": "",
        },
        "d63ca195-3168-11ea-a9c2-021785291289": {
            "station_id": "d63ca195-3168-11ea-a9c2-021785291289",
            "lon": -82.940239,
            "lat": 39.957385,
            "name": "Bexley City Hall at Main St",
            "description": "",
        },
        "d63bd118-3168-11ea-a9c2-021785291289": {
            "station_id": "d63bd118-3168-11ea-a9c2-021785291289",
            "lon": -83.0075375,
            "lat": 39.97125,
            "name": "Kilbourne St & Vine St",
            "description": "",
        },
        "c5c08bb4-aff8-4215-a694-b9a7b1641b31": {
            "station_id": "c5c08bb4-aff8-4215-a694-b9a7b1641b31",
            "lon": -83.02459560334682,
            "lat": 39.95896543121186,
            "name": "Broad St & Martin Ave",
            "description": "",
        },
        "d63c3782-3168-11ea-a9c2-021785291289": {
            "station_id": "d63c3782-3168-11ea-a9c2-021785291289",
            "lon": -83.01138,
            "lat": 39.9574,
            "name": "Lucas St & Town St",
            "description": "",
        },
        "d63c6977-3168-11ea-a9c2-021785291289": {
            "station_id": "d63c6977-3168-11ea-a9c2-021785291289",
            "lon": -82.9954235,
            "lat": 39.9577005,
            "name": "4th St & Rich St",
            "description": "",
        },
        "d63c5be3-3168-11ea-a9c2-021785291289": {
            "station_id": "d63c5be3-3168-11ea-a9c2-021785291289",
            "lon": -83.014305,
            "lat": 39.9940515,
            "name": "Neil Ave & 10th Ave",
            "description": "",
        },
        "d63c4527-3168-11ea-a9c2-021785291289": {
            "station_id": "d63c4527-3168-11ea-a9c2-021785291289",
            "lon": -83.0054595,
            "lat": 39.985221,
            "name": "High St & 4th Ave",
            "description": "",
        },
        "d6ee1ec4-b838-464f-acca-8968b0b2671e": {
            "station_id": "d6ee1ec4-b838-464f-acca-8968b0b2671e",
            "lon": -82.9682765,
            "lat": 40.00075,
            "name": "St. Stephen's Community House",
            "description": "",
        },
        "1347067b-332c-4291-89c9-948813957304": {
            "station_id": "1347067b-332c-4291-89c9-948813957304",
            "lon": -82.9811075,
            "lat": 39.99355,
            "name": "Linden Transit Center",
            "description": "",
        },
        "d63c7b8b-3168-11ea-a9c2-021785291289": {
            "station_id": "d63c7b8b-3168-11ea-a9c2-021785291289",
            "lon": -83.027448,
            "lat": 39.985822,
            "name": "Market District & 3rd Ave",
            "description": "",
        },
        "d63c49b8-3168-11ea-a9c2-021785291289": {
            "station_id": "d63c49b8-3168-11ea-a9c2-021785291289",
            "lon": -82.999556,
            "lat": 39.9887625,
            "name": "Weinland Park - 6th Ave",
            "description": "",
        },
        "d63bba47-3168-11ea-a9c2-021785291289": {
            "station_id": "d63bba47-3168-11ea-a9c2-021785291289",
            "lon": -83.001614,
            "lat": 39.9685285,
            "name": "Sensenbrenner Park",
            "description": "",
        },
        "d63be41b-3168-11ea-a9c2-021785291289": {
            "station_id": "d63be41b-3168-11ea-a9c2-021785291289",
            "lon": -82.9908015,
            "lat": 39.969191,
            "name": "Cleveland Ave & Mt Vernon Ave",
            "description": "",
        },
        "d63d0c70-3168-11ea-a9c2-021785291289": {
            "station_id": "d63d0c70-3168-11ea-a9c2-021785291289",
            "lon": -83.009456,
            "lat": 39.9869065,
            "name": "Thompson Park at Hunter Ave",
            "description": "",
        },
        "d63cc63d-3168-11ea-a9c2-021785291289": {
            "station_id": "d63cc63d-3168-11ea-a9c2-021785291289",
            "lon": -83.0489765,
            "lat": 39.9819315,
            "name": "Grandview Library at Oakland Ave",
            "description": "",
        },
        "1527221109859631254": {
            "station_id": "1527221109859631254",
            "lon": -83.0041135,
            "lat": 39.9567944,
            "name": "Bicentennial Public Rack",
            "description": "Milestone 229, 229, South Civic Center Drive, River South, Columbus, Franklin County, Ohio, 43215, United States",
        },
        "1475694115961709530": {
            "station_id": "1475694115961709530",
            "lon": -83.004018,
            "lat": 39.980002,
            "name": "High & Prescott",
            "description": "Arch City Tavern, 862, North High Street, Italian Village, Columbus, Franklin County, Ohio, 43215, United States of America",
        },
        "1475694107371774928": {
            "station_id": "1475694107371774928",
            "lon": -83.003107,
            "lat": 39.975462,
            "name": "High & Russell",
            "description": "Brandt-Roberts Gallery, 642, North High Street, Italian Village, Columbus, Franklin County, Ohio, 43215, United States of America",
        },
        "1475694115961709532": {
            "station_id": "1475694115961709532",
            "lon": -83.004433,
            "lat": 39.980953,
            "name": "High & Price/First",
            "description": "921, North High Street, Italian Village, Columbus, Franklin County, Ohio, 43201, United States of America",
        },
        "1475697167647006232": {
            "station_id": "1475697167647006232",
            "lon": -83.007939,
            "lat": 39.997555,
            "name": "Ohio State Student Union",
            "description": "Ohio Union, 1739, North High Street, Indianola Terrace, Columbus, Franklin County, Ohio, 43210, United States of America",
        },
        "1475694111666742228": {
            "station_id": "1475694111666742228",
            "lon": -83.003368,
            "lat": 39.976781,
            "name": "High & Lincoln",
            "description": "CoGo High St and Lincoln St, East Lincoln Street, Italian Village, Columbus, Franklin County, Ohio, 43215-1430, United States of America",
        },
        "1475694111666742232": {
            "station_id": "1475694111666742232",
            "lon": -83.003787,
            "lat": 39.978914,
            "name": "High & Hubbard",
            "description": "Moxy, 810, North High Street, Italian Village, Columbus, Franklin County, Ohio, 43215, United States of America",
        },
    }

    def test_read_free_bikes(self):
        free_bikes, update = gbfs.read_enabled_free_bikes("tests_data/free_bike_status.json")
        assert free_bikes == self.exemple_free_bikes

    def test_next_free_bikes(self):
        next_bikes, update = next(gbfs.iter_free_bikes(Path("tests_data/history")))
        assert next_bikes == self.exemple_free_bikes, next_bikes
        
    def test_iter_free_bikes(self):
        it = gbfs.iter_free_bikes(Path("tests_data/history"))
        bikes1, _ = next(it)
        assert bikes1 == self.exemple_free_bikes, next_bikes
        bikes2, _ = next(it)
        assert bikes2 != self.exemple_free_bikes, next_bikes
        nb_items_left = sum(1 for _ in it)
        assert(nb_items_left == 2)
        

    def test_read_stations(self):
        p = Path("tests_data/station_information.json")
        with p.open() as f:
            stations = gbfs.read_stations(f.read())
        assert stations == self.example_stations, stations

    def test_find_nearest_station(self):
        p = Path("tests_data/station_information.json")
        with p.open() as f:
            stations = gbfs.read_stations(f.read())
            nearest, dist = trips.find_nearest_station(-83, 40, stations)
            assert nearest == {'station_id': 'd63cde22-3168-11ea-a9c2-021785291289', 'lon': -83.0011625, 'lat': 40.001957, 'name': 'Summit St & 17th Ave', 'description': ''}, nearest

    def test_find_nearest_no_stations(self):
        nearest, dist = trips.find_nearest_station(-83, 40, {})
        assert nearest is None, nearest
            
    def test_fmain_loop(self):
        free_bikes_iterator = gbfs.iter_free_bikes(Path("tests_data/history"))
        p = Path("tests_data/station_information.json")
        with p.open() as f:
            stations = gbfs.read_stations(f.read())
        for trip in trips.trips_iterator(free_bikes_iterator, stations):
                print(trip)
            
    def test_dt(self):
        year,month,day,hour = outputs.date_time_parts(1647361820)
        assert year == "2022", year
        assert month == "3", month
        assert day == "15", day
        assert hour == "17", hour
        
    def test_format_timestamp(self):
        ts = 1588306501
        f = outputs.format_ts(ts)
        assert f == "2020-05-01 06:15:01.000000+00:00", f



if __name__ == "__main__":
    unittest.main()
