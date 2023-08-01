import sqlite3

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


#UNTUK INSERT DAN UPDATE
# try:
#     sql = 'INSERT INTO DataSiswa (NoAbsen, Nama, JenisKelamin, Umur) VALUES (19, "NARUTO", "L", 26)'
#     sql = 'UPDATE DataSiswa SET Umur=26, NoAbsen=52 WHERE Nama = "NOBITA"'
#     cursor = con.cursor().execute(sql)
#     con.commit() #menyimpan hasil eksekusi sql
#     print("Suskes Eksekusi")
# except Exception as e:
#     print("ERROR insert => " + str(e))

#SELECT DARI DATABASE
try:
    # parameter['NoAbsen'] = 20
    # parameter['Nama'] = "Dora"
    # parameter['JenisKelamin'] = "P"
    # parameter['Umur'] = 52
    # print(parameter)
    
    # parameter2 = { #exist dictionary
    #     'NoAbsen' : 20,
    #     'Nama' : "Dora",
    #     'JenisKelamin' : "P",
    #     'Umur' : 52
    # }
    # print(parameter2)
    # parameter2['Kota'] = "Jakarta"
    # print(parameter2)
    # parameter2.pop('Umur')
    # print(parameter2)
    parameter = {}  #empty dictionary
    parameter['NoAbsen'] = 20
    parameter['Nama'] = "Dora"
    parameter['JenisKelamin'] = "P"
    parameter['Umur'] = 52
 
    #sql = 'SELECT * FROM DataSiswa'
    sql2 = 'INSERT INTO DataSiswa (NoAbsen, Nama, JenisKelamin, Umur) VALUES (19, "NARUTO", "L", 26)'       #syntax sql standar
    
    #sql = 'INSERT INTO DataSiswa (NoAbsen, Nama, JenisKelamin, Umur) VALUES (:NoAbsen, :Nama, :JenisKelamin, :Umur)'    #syntax sql dengan paramter
    cursor = con.cursor().execute(sql)
    con.commit()
    print("succes insert data dengan parameter => " + str(parameter))
    #result = cursor.fetchall()
    #print(result)
    #print(type(result))
    #print(len(result))
    #print("\n")  #escape sequence
    
    # data1 = result[0]
    # print(data1)
    # print(type(data1))
    # namaSiswa = data1['Nama']
    # print(namaSiswa)
except Exception as e:
    print("ERROR insert => " + str(e))
