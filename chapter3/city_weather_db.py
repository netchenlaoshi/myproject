import pymongo
<<<<<<< HEAD

class HefengDb():
=======
import time

class HeFengDb():

>>>>>>> 7a339e53adc5392cac0a74a4bf160861ae12272b
    def __init__(self):
        self.client = pymongo.MongoClient('localhost', 27017)
        self.book_weather = self.client['weather']
        self.sheet_weather = self.book_weather['sheet_weather_3']

<<<<<<< HEAD
=======
    def save_all(self,weathers):
        for each in weathers:
            self.sheet_weather.save(each)

>>>>>>> 7a339e53adc5392cac0a74a4bf160861ae12272b
    def save(self,data):
        self.sheet_weather.insert_one(data)

    def show_all(self):
<<<<<<< HEAD
        all=self.sheet_weather.find()
        for each in all:
            print(each)

    def find(self, condition):
        return  self.sheet_weather.find(condition)

    def delete(self):
        self.sheet_weather.delete_many({})

    def save_all(self, weathers):
        for each in weathers:
            self.save(each)

    def count(self):
        all=self.sheet_weather.find()
        nums=0
        for each in all:
            nums=nums+1
        return nums

if __name__=="__main__":
    hefengDb=HefengDb()
    hefengDb.save({"name":"chenlaoshi","class":"net19049"})
    hefengDb.show_all()
=======
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

>>>>>>> 7a339e53adc5392cac0a74a4bf160861ae12272b
