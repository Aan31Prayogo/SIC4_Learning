from pymongo.mongo_client import MongoClient
import time

uri = "mongodb+srv://prayogoaan:SlXg2lmR2tTQ0iDh@cluster0.hr3gng9.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri)
db = client['SIC4']
my_collection = db['MentorAan'] # diganti sesuai nomor kelompok 


data_sensor = {
    'temp' : 11,
    'hum' : 12,
    'createdAt' : int(time.time())
}
 
result = my_collection.insert_one(data_sensor)
print(result)