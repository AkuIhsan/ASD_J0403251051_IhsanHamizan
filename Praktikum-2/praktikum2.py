#===========================================================
# Praktikum 2 : Konsep ADT  dan File Handling (STUDI KASUS)
# Latihan   1 : Membuat Fungsi Load Data dari File
#===========================================================

#variabel menyimpan data
nama_file = "data_mahasiswa.txt"


def baca_data(nama_file:str) -> dict  :
    data_dict:dict = {}
    with open(nama_file, 'r', encoding='utf-8') as file :
        for baris in file :
            baris:str = baris.strip()
            nim, nama, nilai= baris.split(',')
            data_dict[nim] = {
                'nama'  : nama,
                'nilai' : nilai
            }

    return data_dict



#===========================================================
# Praktikum 2 : Konsep ADT  dan File Handling (STUDI KASUS)
# Latihan   2 : Membuat Fungsi Menampilkan Data
#===========================================================


def tampilkan_data(data) -> str :
    #Membuat Header Tabel
    print("\n=== Daftar Mahasiswa ===")
    print(f"{'NIM'  :<10} | {'Nama'  :<12} | {'Nilai'  :>5}")
    print('-'*35)

    for nim in sorted(data.keys()) :
        nama = data[nim]["nama"]
        nilai = data[nim]['nilai']
        print(f"{nim:<10} | {nama:<12} | {int(nilai):>5}")



#===========================================================
# Praktikum 2 : Konsep ADT  dan File Handling (STUDI KASUS)
# Latihan   3 : Membuat Fungsi Mencari Data
#===========================================================

#membuat fungsi pencaraian data
def cari_data(data) :
    #pencarian data berdasarkan nim sebagai key dictionary
    #membuat input nim mahasiswa yang akan dicari
    nim_cari = input("Masukkan NIM mahasiswa yang ingin dicari: ").strip()

    if nim_cari in data :
        nama = data[nim_cari]['nama']
        nilai = data[nim_cari]['nilai']

        print("===== Data Mahasiswa Ditemukan =====")
        print(f"NIM    : {nim_cari}")
        print(f"Nama   : {nama}")
        print(f"Nilai  : {nilai}")

    else :
        print("data tidak ditemukan. Pastikan NIM yang dimasukkan benar")




#===========================================================
# Praktikum 2 : Konsep ADT  dan File Handling (STUDI KASUS)
# Latihan   4 : Membuat Fungsi Update Data
#===========================================================

#membuat fungsi update data
def ubah_data(data) :

    #awali dulu mencari nim / data mahasiswa yang ingin di update
    nim = input("Masukkan NIM mahasiswa yang ingin diubah datanya : ").strip()

    if nim not in data :
        print("NIM tidak ditemukan. Update dibatalkan")
        return
    
    try:
        nilai_baru = int(input("Masukkan nilai baru. 0-100 : ").strip())
    except ValueError :
        print("Nilai harus berupa angka. Update Dibatalkan")

    if nilai_baru < 0 or nilai_baru > 100 :
        print("Nilai harus antara 0 sampai 100 Update dibatalkan")
        return

    nilai_lama = data[nim]['nilai']
    data[nim]["nilai"] = nilai_baru

    print(f"Update Berhasil. Nilai {nim} berubah dari {nilai_lama} menjadi {nilai_baru}")


#===========================================================
# Praktikum 2 : Konsep ADT  dan File Handling (STUDI KASUS)
# Latihan   5 : Membuat Fungsi Meniympan Data pada File
#===========================================================

#membuat fungsi menyimpan data ke File
def simpan_data(nama_file, data) :
    with open(nama_file,"w", encoding="utf-8") as file :
        for nim in sorted(data.keys()) :
            nama = data[nim]['nama']
            nilai = data[nim]['nilai']
            file.write(f"{nim},{nama},{nilai}\n")


#===========================================================
# Praktikum 2 : Konsep ADT  dan File Handling (STUDI KASUS)
# Latihan   6 : Membuat Menu Interaktif
#===========================================================

def main() :
    #load data otomatis saat prgoram dimulai
    data_mahasiswa = baca_data(nama_file=nama_file) 

    while True:
        print("\n=== MENU DATA MAHASISWA===")
        print("1. Tampilkan Data Mahasiswa")
        print("2. Cari data mahasiswa")
        print("3. Ubah Nilai Mahasiswa")
        print("4. Simpan Data ke File")
        print("0. Keluar")

        pilihan = input("Pilih Menu: ").strip()

        if pilihan == "1" :
            tampilkan_data(data=data_mahasiswa)
        elif pilihan == "2" :
            cari_data(data=data_mahasiswa)
        elif pilihan == "3" :
            ubah_data(data=data_mahasiswa)
        elif pilihan == "4" :
            simpan_data(nama_file=nama_file, data=data_mahasiswa)
        elif pilihan == "0" :
            print("Program Selesai.")
            break
        else :
            print("pilihan tidak valid. Silahkan Coba Lagi")

if __name__ == "__main__" :
    main()