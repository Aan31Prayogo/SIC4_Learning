import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from time import sleep     # Import the sleep function from the time module

pin_sensor = 16  #ganti sesuai pin yang digunakan

GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering
GPIO.setup(pin_sensor, GPIO.IN)

def bacaSensor():
    while True:
        smoke_level = GPIO.input(pin_sensor)
        print("[INFO] smoke level = ", smoke_level)
        sleep(3)

if __name__ == "__main__":
    bacaSensor()
