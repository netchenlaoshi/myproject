import unittest

from chapter3.city_weather import HeFeng
from chapter3.city_weather_db import HefengDb


class TestCityWeatherDbCase(unittest.TestCase):

    def test_save(self):
        hefengDb = HefengDb()
        hefengDb.save({"name": "chenlaoshi", "class": "net19049"})
        hefengDb.show_all()
        results=hefengDb.find({"name":"chenlaoshi"})
        for each in results:
            self.assertEqual("chenlaoshi",each['name'])
            self.assertEqual("net19049",each['class'])
        hefengDb.delete()
            # print(each)
        # self.assertEqual(4,hefengDb.find_all())

    def test_save_all(self):
        hefeng=HeFeng()
        # codes=hefeng.get_city_code()
        # for each in codes:
        #     print(next(codes))
        each=hefeng.get_weather("CN101010200")
        print(each)
        hefengDb=HefengDb()
        hefengDb.save(each)

if __name__ == '__main__':
    unittest.main()
