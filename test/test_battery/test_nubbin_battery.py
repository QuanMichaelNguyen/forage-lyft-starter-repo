import unittest
from datetime import date

from battery.nubin_battery import NubbinBattery



class TestNubbinBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = date.fromisoformat("2024-01-20")
        last_service_date = date.fromisoformat("2020-12-15")
        battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = date.fromisoformat("2024-01-20")
        last_service_date = date.fromisoformat("2023-12-15")
        battery = NubbinBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())