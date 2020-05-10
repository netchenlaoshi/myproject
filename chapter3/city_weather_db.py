import pymongo
import time

class HeFengDb():

    def __init__(self):
        self.client = pymongo.MongoClient('localhost', 27017)
        self.book_weather = self.client['weather']
        self.sheet_weather = self.book_weather['sheet_weather_3']

    def save_all(self,weathers):
        for each in weathers:
            self.sheet_weather.save(each)

    def save(self,data):
        self.sheet_weather.insert_one(data)

    def show_all(self):
        results=self.sheet_weather.find()
        for each in results:
            print(each.__next__())

    def __del__(self):
        # self.book_weather.drop_collection(self.sheet_weather)
        pass


if __name__ == '__main__':
    hefeng_db=HeFengDb()
    data={"name":"chenlaoshi","age":"18"}
    hefeng_db.save(data)
    hefeng_db.show_all()
    # del(hefeng_db)

