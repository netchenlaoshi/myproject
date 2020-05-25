import unittest

from chapter3.city_weather import HeFeng


<<<<<<< HEAD
class CityWeatherTest(unittest.TestCase):
    def test_get_city_code(self):
        hefeng=HeFeng()
        codes=hefeng.get_city_code()
        print(codes)
        count=0
        for each in codes:
            print(next(codes))
            count+=1
        print("count=",count)
        self.assertEqual(1620, count)

    def test_get_all_weather(self):
        hefeng=HeFeng()
        results=hefeng.get_all_weather(7)
        # print(results)
        for each in results:
            print(each)
        self.assertEqual(7,len(results))
=======
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


>>>>>>> 7a339e53adc5392cac0a74a4bf160861ae12272b

if __name__ == '__main__':
    unittest.main()
