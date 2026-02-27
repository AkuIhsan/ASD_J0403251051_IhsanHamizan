# ==========================================================
# Latihan 4: Kombinasi Huruf 
# Nama : IHSAN HAMIZAN
# Nim : J0403251051
# Kelas : TPL A2
# ==========================================================
def kombinasi(n, hasil=""):
    # Mengecek apakah panjang hasil sama dengan n, jika iya maka masuk ke base case untuk mencetak hasilnya
    if len(hasil) == n:
        print(hasil)
        return
    # Recursive call ini akan di jalankan terlebih sampai menyetuh base case 
    kombinasi(n, hasil + "A")
    # Recursive call ini akan di jalankan, jika recursive call sebelumnya sudah selesai samapai base case
    kombinasi(n, hasil + "B")

kombinasi(2)

# Rangkuman mekanisme jumlah kombinasi yang dihasilkan
# gambaran kode seperti ini untuk jumlah kombinasinya bisa dihitung menggunakan rumus 2 pangkat n 
# n = 2 hasil = ""
    # n = 2 hasil = "A"
        # n = 2 hasil = "AA" -> panjang hasil sudah sama dengan nilai n
        # n = 2 hasil = "AB" -> panjang hasil sudah sama dengan nilai n
    # n = 2 hasil = "B"
        # n = 2 hasil = "BB" -> panjang hasil sudah sama dengan nilai n
        # n = 2 hasil = "BA" -> panjang hasil sudah sama dengan nilai n