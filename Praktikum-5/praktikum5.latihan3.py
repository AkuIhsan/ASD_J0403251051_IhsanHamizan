# ==========================================================
# Latihan 3: Mencari Nilai Maksimum
# Nama : IHSAN HAMIZAN
# Nim : J0403251051
# Kelas : TPL A2
# ==========================================================
def cari_maks(data, index=0):
    # Base case
    if index == len(data) - 1:
        return data[index]
    # Recursive case
    maks_sisa = cari_maks(data, index + 1)
    if data[index] > maks_sisa:
        return data[index]
    else:
        return maks_sisa
angka = [3, 7, 2, 9, 5]
print("Nilai maksimum:", cari_maks(angka))

# Rangkuman alur program, base case dan recursive call
# program ini mencari nilai maksimal dengan membandingkan nilai terakhir dengan nilai sebelumnya, jika nilai terakhir lebih besar dari pada nilai sebelumnya
# maka kembalikan nilai terkahir tersebut, namaun jika nilai terkhir lebih kecil dari pada nilai sebelumnnya maka kembalikan nilai sebelumnya, lalu bandingkan
# sampai ke index pertama atau awal, jika kondisi index sama dengan panjang data dikurang satu maka dia memasuki base case jika tidak dia akan lanjut ke recursive call
