from django.test import TestCase
from django.test import SimpleTestCase
from .state_machine import is_safe_green_configuration


class TrafficSafetyTests(SimpleTestCase):

    def test_north_south_can_be_green(self):
        self.assertTrue(
            is_safe_green_configuration(["NORTH", "SOUTH"])
        )

    def test_east_west_can_be_green(self):
        self.assertTrue(
            is_safe_green_configuration(["EAST", "WEST"])
        )

    def test_conflicting_phases_cannot_be_green(self):
        self.assertFalse(
            is_safe_green_configuration(["NORTH", "EAST"])
        )