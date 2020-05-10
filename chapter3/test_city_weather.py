import unittest

from chapter3.city_weather import HeFeng


class TestCityWeather(unittest.TestCase):

    def test_city_codes(self):
        hefeng = HeFeng()
        codes = hefeng.get_city_code()
        count = 0
        for each in codes:
            count = count + 1
            print(codes.__next__())
        print("count=", count)
        self.assertEqual(1620, count)

    def test_city_weather(self):
        hefeng=HeFeng()
        result=hefeng.today_weather("CN101120704")
        print(result.keys())
        self.assertIn('cloud',result)

    def test_all_weather(self):
        hefeng=HeFeng()
        result=hefeng.get_all_weather()
        self.assertEqual(10,len(result))



if __name__ == '__main__':
    unittest.main()
