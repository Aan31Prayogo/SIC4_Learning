from flask import Flask, request, jsonify
from pymongo.mongo_client import MongoClient
import time

uri = "mongodb+srv://prayogoaan:SlXg2lmR2tTQ0iDh@cluster0.hr3gng9.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)
app = Flask(__name__)

@app.route("/sensor" , methods = ['POST'])
def store_sensor():
    res = {}
    try:
        #parsing data dari Insomnia / Postman
        data = request.json
        print(data)
        temp = data['temp']
        hum = data['hum']
        #createdAt = data['createdAt']
        
        db = client['SIC4']
        my_collection = db['MentorAan'] # diganti sesuai nomor kelompok 
        
        data_sensor = {
           'temp' : temp,
           'hum' : hum,
           'createdAt' : int(time.time())
        }
        my_collection.insert_one(data_sensor)
        res['isSucces'] = True
        res['data'] = data_sensor
        res['message'] = ""
        return jsonify (res),200
    except Exception as e:
        res['isSucces'] = False
        res['data'] = ""
        res['message'] = e
        print(res)
        return jsonify (res),500

if __name__ == "__main__":
    app.run()
        