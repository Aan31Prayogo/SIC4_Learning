import sqlite3
import time
from datetime import datetime

DB_NAME = "DatabaseKelas.db"
con = False

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


con = sqlite3.connect(DB_NAME)  #membuat koneksi python ke Database
con.row_factory = dict_factory
print("\n")

if con:
    print("Sukses konek ke DB")
else:
    print("Gagal konek DB")

def insert_datasiswa(parameter):
    try:  
        sql = 'INSERT INTO DataSiswa (NoAbsen, Nama, JenisKelamin, Umur) VALUES (:NoAbsen, :Nama, :JenisKelamin, :Umur)'    #syntax sql dengan paramter
        cursor = con.cursor().execute(sql, parameter)
        con.commit()
        print("succes insert data dengan parameter => " + str(parameter))
    except Exception as e:
        print("ERROR insert => " + str(e))
        
siswa1 = {}
siswa1['NoAbsen'] = 13
siswa1['Nama'] = "Micko"
siswa1['JenisKelamin'] = "L"
siswa1['Umur'] = 12

siswa2 = {}
#siswa2['NoAbsen'] = 13
siswa2['Nama'] = "Minie"
siswa2['JenisKelamin'] = "P"
siswa2['Umur'] = 11

datasiswa = []
datasiswa.append(siswa1)
datasiswa.append(siswa2)
#print(datasiswa)

for siswa in datasiswa:
    insert_datasiswa(siswa)
    time.sleep(1)




