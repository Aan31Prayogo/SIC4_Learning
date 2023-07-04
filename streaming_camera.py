import cv2

#droidcam = "192.168.0.123"   #RTSP

cam = cv2.VideoCapture(5)  #default 0 untuk webcam laptop
                            #selain 0 (1), (2) untuk webcam


cam = cv2.VideoCapture()
while True:
    ret, frame = cam.read()
    
    if not ret:
        print("failed to open camera")
        break
    
    cv2.imshow("streaming camera", frame) 
    
    #ASCII
    
    key = cv2.waitKey(1) & 0xFF   # membaca input keyboard dari pengguna
    
    if key==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()