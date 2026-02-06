#============================================================
# Praktikum 1 : konsep ADT dan File Handling
# Latihan Dasar 1 : Membaca seluruh isi file data
#============================================================

print("====Membuka file dalam satu string====")
with open('data_mahasiswa.txt', 'r', encoding='utf-8' ) as file :
    isi_file = file.read()

print(isi_file)
print("Tipe Data :",type(isi_file))

#============================================================
# Praktikum 1 : konsep ADT dan File Handling
# Latihan Dasar 2 : Membaca seluruh isi file data dengan cara per baris
#============================================================

print("====Membuka file per baris====")
jumlah_baris = 0 #inisiasi variabel untuk menghitung jumlah baris
with open("data_mahasiswa.txt","r", encoding="utf-8") as file :
    for baris in file :
        jumlah_baris = jumlah_baris + 1
        baris= baris.strip()
        print("Baris ke-", jumlah_baris)
        print("isinya :", baris)




#============================================================
# Praktikum 1 : konsep ADT dan File Handling
# Latihan Dasar 3 : Membaca data dan menyimpannya ke struktur list
#============================================================

data_list = [] # inisiasi list untuk menampung data

with open("data_mahasiswa.txt","r", encoding="utf-8") as file :
    for baris in file :
        baris = baris.strip() # menghilangkan karakter baris baru
        nim, nama, nilai = baris.split(",") # memecah data menjadi satuan
        data_list.append([nim, nama, int(nilai)])
        print(f'NIM : {nim}, Nama : {nama}, nilai {nilai}') 

print("====menampilkan data list====")
print(data_list)

print("contoh record ke 1 ", data_list[0])
print("contoh record ke 2 ", data_list[1])
print("Jumlah record", len(data_list))

#============================================================
# Praktikum 1 : konsep ADT dan File Handling
# Latihan Dasar 4 : Membaca dan menyimpan data dalam struktur dictionary
#============================================================

data_list = {} # inisiasi dictionary untuk menyimpan data
with open("data_mahasiswa.txt","r", encoding="utf-8") as file :
    for baris in file :
        baris = baris.strip() # menghilangkan karakter baris baru
        nim, nama, nilai = baris.split(",") # memecah data menjadi satuan
        #simpan data dalam dictionary
        data_list[nim] = {
            "Nama" : nama,
            "Nilai" : int(nilai),
        }

print(data_list)