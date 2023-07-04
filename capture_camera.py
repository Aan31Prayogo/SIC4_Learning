import cv2
from datetime import datetime
import os
#droidcam = "192.168.0.123"   #RTSP

cam = cv2.VideoCapture(1)  #default 0 untuk webcam laptop
                            #selain 0 (1), (2) untuk webcam

path = os.getcwd()

while True:
    ret, frame = cam.read()
    
    if not ret:
        print("failed to open camera")
        break
    
    cv2.imshow("streaming camera", frame) 
    
    #ASCII
    
    key = cv2.waitKey(1) & 0xFF   # membaca input keyboard dari pengguna
    
    if key==ord('q'):
        print("quit by keyboard")
        break
    if key==ord('c'):  #ketika pencet C akan capture kamera
        #name_file = "test.jpg"
        nama_file = datetime.now().strftime("%Y:%m:%d_%h:%m:%S")
        image = cv2.imwrite(path + "/" + nama_file + ".jpg", frame)    #fungsi untuk menyimpan gambar
        print("sukses simpan gambar denga nama file ", nama_file)
        

cam.release()
cv2.destroyAllWindows()