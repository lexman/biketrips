import unittest
import main
from pathlib import Path


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

    def test_read_free_bikes(self):
        free_bikes = main.read_enabled_free_bikes("tests_data/free_bike_status.json")
        assert free_bikes == self.exemple_free_bikes

    def test_next_free_bikes(self):
        next_bikes = main.get_next_free_bikes(Path("tests_data/history"))
        assert next_bikes == self.exemple_free_bikes


if __name__ == "__main__":
    unittest.main()
