import cv2
from pyzbar.pyzbar import decode
#import RPi.GPIO as GPIO
import requests
from datetime import datetime
import os
import sqlite3
import threading

cap = cv2.VideoCapture(0)
face_classifier=cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
#face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# GPIO.setwarnings(False)
# LED_MERAH = 8
# LED_HIJAU = 10

# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(LED_MERAH, GPIO.OUT, inital= GPIO.LOW)
# GPIO.setup(LED_HIJAU, GPIO.OUT, inital= GPIO.LOW)

TELEGRAM_TOKEN = "5936063047:AAEegGclhoRYVF2AnKsnWlAn-g0uwgLvT6o"
CHAT_ID_TELEGRAM = "672670660"

path = os.getcwd() + "/capture"
DB_NAME = "sawiremah.db"

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def capture_image():
    global frame
    try:
        dt_string = datetime.now().strftime("%Y:%m:%d_%h:%m:%S")
        nama_file = dt_string + ".jpg"
        image = cv2.imwrite(path + "/" + nama_file, frame)    #fungsi untuk menyimpan gambar
        print("sukses simpan gambar denga nama file ", nama_file)
        start_send_image_to_telegram(nama_file)
    except Exception as e:
        print(f'[FAILED] capture_image= {e}' )

def start_send_image_to_telegram(file_img):
    t2 = threading.Thread(target=send_image_to_telegram, args=(file_img,))
    t2.start()
    
def send_image_to_telegram(file_img):	
	try:
		TOKEN = TELEGRAM_TOKEN  #token bot kelompok
		chat_id = CHAT_ID_TELEGRAM #ganti chat id pengguna
		image=open(path+'/'+file_img,'rb')
		url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto?chat_id={chat_id}"
		resp=requests.get(url,files={'photo':image}) 

		if int(resp.status_code)==200:
			print('succes send to telegram')

	except Exception as e:
		print(f'[FAILED] send image to telegram with error = {e}' )
  
def start_send_msg_to_telegram(text):
    t1 = threading.Thread(target=send_image_to_telegram, args=(text,))
    t1.start()
    
def send_msg_to_telegram(text):
    try:
        token = TELEGRAM_TOKEN
        chat_id = CHAT_ID_TELEGRAM
        url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text 
        results = requests.get(url_req)
        #print(results.json())
        if int(results.status_code)==200:
            print('succes send msg to telegram')
    except Exception as e:
        print(f'[FAILED] send msg to telegram with error = {e}' )

def open_camera():
    global frame
    global stopFlag
    last_qr_data = ""
    
    con = False
    con = sqlite3.connect(DB_NAME)  #membuat koneksi python ke Database
    con.row_factory = dict_factory
    print("\n")

    if con:
        print("Sukses konek ke DB")
    else:
        print("Gagal konek DB")
    
    while True:
        ret, frame = cap.read()
        frame = cv2.resize(frame,(480,480))
        
        if not ret :
            print("failed to open camera")
            #GPIO.cleanup() # cleanup all GPIO 
            break
        
        gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray_image, 1.2, 4)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
           
            qr_raw=decode(frame)
                
            for detect in qr_raw:
                (x, y, w, h) = detect.rect
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)
                qr_data=detect.data.decode("utf-8")
                #print(qr_data)
                
                if qr_data != last_qr_data:
                    param = {'id' : qr_data}
                    sql = 'SELECT * FROM DataSiswa WHERE id=:id'
                    cursor = con.cursor().execute(sql,param)
                    result = cursor.fetchall()
                    #print(result)
                    
                    nama = result[0]['nama']
                    txt_msg = "Nama = " + nama 
                    capture_image() 
                    start_send_msg_to_telegram(txt_msg)
                    last_qr_data= qr_data

        cv2.imshow("streaming camera", frame) 
            
            
        key = cv2.waitKey(1) & 0xFF   # membaca input keyboard dari pengguna
        
        if key==ord('q'):
            print("quit by keyboard")
            break
        if key==ord('c'):  #ketika pencet C akan capture kamera
            #name_file = "test.jpg"
            nama_file = datetime.now().strftime("%Y:%m:%d_%h:%m:%S")
            image = cv2.imwrite(path + "/" + nama_file + ".jpg", frame)    #fungsi untuk menyimpan gambar
            print("sukses simpan gambar denga nama file ", nama_file)

if __name__ == '__main__':
    try:
        if not os.path.exists(path):
            print("[INFO] Membuat folder capture")
            os.mkdir(path)
        else:
            print("[INFO] folder capture sudah terbentuk")

        open_camera() #running dengan menggunakan threading
        #read_rfid()
    except KeyboardInterrupt:
        #GPIO.cleanup() # cleanup all GPIO 
        print("close")