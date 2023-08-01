#import library yang dibutuhkan
import threading            #library multithreading
import time


def start_timetout1(durasi):
    t1 = threading.Thread(target=timetout1, args=(durasi,))
    t1.start()

def start_timetout2():
    t1 = threading.Thread(target=timetout2)
    t1.start()

def timetout1(durasi):
    count = durasi
    print("timeout 1 mulai")

    while count>0:
        print(f"timeout 1 count {count}")
        count-=1
        time.sleep(1)
        
    print("timeout 1 selesai")
    
def timetout2(durasi):
    count = durasi
    print("timeout 2 mulai")

    while count>0:
        print(f"timeout 2 count {count}")
        count-=1
        time.sleep(1)
        
    print("timeout 2 selesai")


#timetout1(2)
start_timetout1(4)  #multithreading
#start_timetout2()    #multithreading


# def print_kata(kata = "Hello"):
#     print(f"ini dari argument fungsi {kata}")

# print_kata("SIC 4 bootcamp")
