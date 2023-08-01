from flask import Flask, request, jsonify
from pymongo.mongo_client import MongoClient
import time

uri = "mongodb+srv://prayogoaan:SlXg2lmR2tTQ0iDh@cluster0.hr3gng9.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)
app = Flask(__name__)

@app.route("/sensor" , methods = ['POST'])
def store_sensor():
    try:
        #parsing data dari INsomnia / POstman
        data = request.json
        temp = data['temp']
        hum = data['hum']
        createdAt = data['createdAt']
        
        db = client['SIC4']
        my_collection = db['MentorAan'] # diganti sesuai nomor kelompok 
        
        data_sensor = {
           'temp' : temp,
           'hum' : hum,
           'createdAt' : createdAt
        }
        my_collection.insert_one(data_sensor)
        return jsonify ({'isSucces' : True})
    except Exception as e:
        return jsonify ({'isSucces' : False})

if __name__ == "__main__":
    app.run()
        