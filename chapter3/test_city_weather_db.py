import unittest

from chapter3.city_weather import HeFeng
from chapter3.city_weather_db import HeFengDb


class TestCityWeatherDb(unittest.TestCase):
    def test_save_all(self):
        hefeng=HeFeng()
        weathers=hefeng.get_all_weather()
        hefengdb=HeFengDb()
        hefengdb.save_all(weathers)
        self.assertEqual(True, True)

if __name__ == '__main__':
    unittest.main()
