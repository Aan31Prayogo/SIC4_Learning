import time
import requests
import math
import random
from gpiozero import PWMLED, MCP3008
from time import sleep
import requests
#import RPi.GPIO as GPIO

# GPIO.setwarnigs(False)
# PIR = 14

# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(PIR, GPIO.INPUT)

TOKEN = ""  # Put your TOKEN here
DEVICE_LABEL = ""  # Put your device label here 
VARIABLE_LABEL_1 = "smoke detector"  # Put your first variable label here
# VARIABLE_LABEL_2 = "humidity"  # Put your second variable label here
# VARIABLE_LABEL_3 = "pir"  # Put your second variable label here
#create an object called pot that refers to MCP3008 channel 0
pot = MCP3008(0)

#create a PWMLED object called led that refers to GPIO 14
led = PWMLED(14)


def build_payload(variable_1,value):
    # Creates two random values for sending data
    variable_1 = value  #temprature
    # value_2 = random.randint(0, 85) #humidity
    # value_3 = random.randint(0,1)

    payload = {variable_1: value}  #dictionary / JSON

    return payload


def post_request(payload):
    # Creates the headers for the HTTP requests
    url = "http://industrial.api.ubidots.com"
    url = "{}/api/v1.6/devices/{}".format(url, DEVICE_LABEL)
    headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}

    # Makes the HTTP requests
    status = 400
    attempts = 0
    while status >= 400 and attempts <= 5:
        req = requests.post(url=url, headers=headers, json=payload)
        print(req.json())
        status = req.status_code
        attempts += 1
        time.sleep(1)

    # Processes results
    print(req.status_code, req.json())
    if status >= 400:
        print("[ERROR] Could not send data after 5 attempts, please check \
            your token credentials and internet connection")
        return False

    print("[INFO] request made properly, your device is updated")
    return True


def main():
    if(pot.value < 0.001):
        led.value = 0
    else:
        led.value = pot.value
    #print(pot.value)
    valueAsap = round(pot.value * 100, 3)
    #tambahan
    if valueAsap > 3.000 : #minimal_:
        print("[INFO] Asap dan Gas Terdeteksi")

        #Sending notification to Telegram
        text = "[INFO] Asap Terdeksi"
        base_url = 'https://api.telegram.org/bot6305275346:AAFqQKR5VVZvQqERVInyTohvnmjAIJkNULE/sendMessage?chat_id=-970317472&text="{}"'.format(text)
        requests.get(base_url)
    else:
        print("[INFO] Asap Tidak Ada")
#    print(valueAsap)

    payload = build_payload(VARIABLE_LABEL_1, valueAsap)

    print("[INFO] Attemping to send data")
    print("[INFO] send payload to ubidots => " + str(payload))
    post_request(payload)   #kirim data ke ubidots
    print("[INFO] finished")


if __name__ == '__main__':
    while (True):
        main()
        time.sleep(5)
        print("\n")