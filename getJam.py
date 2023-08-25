from datetime import datetime, time

jam = datetime.now().strftime("%H:%M")
istirahat_1_awal = "09.30" 
istirahat_1_akhir = "10.00"
print(jam)
if istirahat_1_awal <=  jam <= istirahat_1_akhir:
    print("CEK MASUK")
else:
    print("CEK CANCEL")