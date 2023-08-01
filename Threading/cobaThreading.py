import time
import threading  #library threading

def start_countdown1():
    t1 = threading.Thread(target= countdown1)
    t1.start()

def start_coutndown2():
    t2 = threading.Thread(target= countdown2)
    t2.start()

def countdown1():
    print("mulai countdown 1")
    i = 5
    while i>0:
        i-=1
        print(f"coutndown 1 => {i}")
        time.sleep(1)
    print("hitung 1 selesai!")
    
def countdown2():
    print("mulai countdown 2")
    i = 3
    while i>0:
        i-=1
        print(f"coutndown 2 => {i}")
        time.sleep(1)
    print("hitung 2 selesai!")

if __name__ == "__main__":
    start_countdown1()
    start_coutndown2()
    