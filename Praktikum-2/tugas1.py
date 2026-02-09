# ========================================================== 
# TUGAS HANDS-ON MODUL 1 
# Studi Kasus: Sistem Stok Barang Kantin (Berbasis File .txt) 
# 
# Nama  : Ihsan Hamizan
# NIM   : J0403251051
# Kelas : A2
# ========================================================== 
# ------------------------------- 
# Konstanta nama file 
# ------------------------------- 
NAMA_FILE = "stok_barang.txt" 
# ------------------------------- 
# Fungsi: Membaca data dari file 
# ------------------------------- 
def baca_stok(nama_file): 
    """ 
    Membaca data stok dari file teks. 
    Format per baris: KodeBarang,NamaBarang,Stok 
    Output: - stok_dict (dictionary) 
    key   = kode_barang 
    value = {"nama": nama_barang, "stok": stok_int} 
    """ 
    stok_dict = {} 
    # TODO: Buka file dan baca seluruh baris 
    # Hint: with open(nama_file, "r", encoding="utf-8") as f: 
    # TODO: Untuk setiap baris: 
    # - gunakan strip() untuk menghilangkan \n 
    # - split(",") untuk memisahkan kolom 
    # - simpan ke dictionary 

    with open(nama_file,'r',encoding="utf-8") as file :

        for baris in file :
            kode,nama,stok = baris.strip().split(",")
            stok_dict[kode] = {"nama" : nama, "stok" : stok}    

    return stok_dict



# ------------------------------- 
# Fungsi: Menyimpan data ke file 
# ------------------------------- 
def simpan_stok(nama_file, stok_dict): 
    """ 
    Menyimpan seluruh data stok ke file teks. 
    Format per baris: KodeBarang,NamaBarang,Stok 
    """ 
    # TODO: Tulis ulang seluruh isi file berdasarkan stok_dict 
    # Hint: with open(nama_file, "w", encoding="utf-8") as f: 
    with open(nama_file,'w',encoding="utf-8") as file :
        for data_barang in stok_dict.keys() :
                file.write(f"{data_barang},{stok_dict[data_barang]['nama']},{stok_dict[data_barang]['stok']}\n")


# ------------------------------- 
# Fungsi: Menampilkan semua data 
# ------------------------------- 
def tampilkan_semua(stok_dict): 
    """ 
    Menampilkan semua barang di stok_dict. 
    """ 
    # TODO: Jika kosong, tampilkan pesan stok kosong 
    # TODO: Tampilkan dengan format rapi: kode | nama | stok 
    if len(stok_dict) == 0 :
        print("kosong")
        return
    
    print(f"{'Kode':<10} | {'Nama':<12} | {'Stok':<10} ")
    for data_barang in stok_dict.keys() :
        kode = data_barang
        nama = stok_dict[data_barang]['nama']
        stok = stok_dict[data_barang]['stok']
        print(f"{kode:<10} | {nama:<12} | {stok:<10}")


# ------------------------------- 
# Fungsi: Cari barang berdasarkan kode 
# ------------------------------- 
def cari_barang(stok_dict): 
    """ 
    Mencari barang berdasarkan kode barang. 
    """ 
    kode = input("Masukkan kode barang: ").strip().upper()
    # TODO: Cek apakah kode ada di dictionary 
    # Jika ada: tampilkan detail barang 
    # Jika tidak ada: tampilkan 'Barang tidak ditemukan' 
    if kode not in stok_dict.keys() :
        print("Barang tidak ditemukan")
        return

    print(f"kode barang adalah {kode}, nama barang adalah {stok_dict[kode]['nama']}, stok barang tersisa {stok_dict[kode]['stok']}")

# ------------------------------- 
# Fungsi: Tambah barang baru 
# ------------------------------- 
def tambah_barang(stok_dict): 
    """ 
    Menambah barang baru ke stok_dict. 
    """ 
    kode = input("Masukkan kode barang baru: ").strip().upper()
    if kode in stok_dict.keys() :
        print("Kode sudah digunakan")
        return
    
    stok = int(input("Masukkan jumlah stok awal: "))
    if stok < 0 :
        print("Stok tidak bole negatif")
        return 
    
    nama = input("Masukkan nama barang: ").strip().capitalize()
    # TODO: Validasi kode tidak boleh duplikat 
    # Jika sudah ada: tampilkan 'Kode sudah digunakan' dan return 
    # TODO: Input stok awal (integer) 
    # Hint: stok_awal = int(input(...)) 
    # TODO: Simpan ke dictionary 
    stok_dict[kode] = {'nama' : nama, 'stok': stok}
    


# ------------------------------- 
# Fungsi: Update stok barang 
# ------------------------------- 
def update_stok(stok_dict): 
    """ 
    Mengubah stok barang (tambah atau kurangi). 
    Stok tidak boleh menjadi negatif. 
    """ 
    kode = input("Masukkan kode barang yang ingin diupdate: ").strip().upper() 
    # TODO: Cek apakah kode ada di dictionary 
    # Jika tidak ada: tampilkan pesan dan return 

    if kode not in stok_dict.keys() :
        print("Kode barang tidak ditemukan")
        return

    stok = int(stok_dict[kode]['stok'])
    print("Pilih jenis update:") 
    print("1. Tambah stok") 
    print("2. Kurangi stok") 

    pilihan = int(input("Masukkan pilihan (1/2): ").strip()) 

    # TODO: Input jumlah perubahan stok 
    # Hint: jumlah = int(input("Masukkan jumlah: ")) 
    # TODO: 
    # - Jika pilihan 1: stok = stok + jumlah 
    # - Jika pilihan 2: stok = stok - jumlah 
    # - Jika hasil < 0: batalkan dan tampilkan error 
    if pilihan == 1 :
        jumlah = int(input("Masukkan jumlah:"))
        if jumlah < 0 :
            print("Tidak boleh negatif")
            return
        stok_dict[kode]['stok'] = stok + jumlah
    elif pilihan == 2 :
        jumlah = int(input("Masukkan jumlah:"))
        if jumlah < 0 :
            print("Tidak boleh negatif")
            return
        stok_dict[kode]['stok'] = stok - jumlah


# ------------------------------- 
# Program Utama 
# ------------------------------- 
def main(): 
    # Membaca data dari file saat program mulai 
    stok_barang = baca_stok(NAMA_FILE) 
    print(stok_barang)
    while True: 
        print("\n=== MENU STOK KANTIN ===") 
        print("1. Tampilkan semua barang") 
        print("2. Cari barang berdasarkan kode") 
        print("3. Tambah barang baru") 
        print("4. Update stok barang") 
        print("5. Simpan ke file") 
        print("0. Keluar") 

        pilihan = input("Pilih menu: ").strip() 

        if pilihan == "1": 
            tampilkan_semua(stok_barang) 

        elif pilihan == "2": 
            cari_barang(stok_barang) 

        elif pilihan == "3": 
            tambah_barang(stok_barang) 

        elif pilihan == "4": 
            update_stok(stok_barang) 

        elif pilihan == "5": 
            simpan_stok(NAMA_FILE, stok_barang) 
            print("Data berhasil disimpan.") 

        elif pilihan == "0": 
            print("Program selesai.") 
            break 
        else: 
            print("Pilihan tidak valid. Silakan coba lagi.")

            
# Menjalankan program utama 
if __name__ == "__main__": 
    main() 