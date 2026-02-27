# ==========================================================
# Latihan 2: Tracing Rekursi
# Nama : IHSAN HAMIZAN
# Nim : J0403251051
# Kelas : TPL A2
# ==========================================================
def countdown(n):
    if n == 0:
        print("Selesai")
        return
    print("Masuk:", n)
    countdown(n - 1)
    print("Keluar:", n)

countdown(3)

# Rangkuman alasan "mengapa output 'keluar' muncul terbalik ?
# Karena ketika ingin melakukan print("Keluar") terhalang oleh fungsi rekursif countdown yang dimana fungsi itu harus di selesaikan hingga ke base case
# ketika sudah mencapai base case maka kode selanjutnya bisa dijalankan
# gambaran kodenya seperti ini
# n = 3
# print("Masuk:", 3)
# print("Masuk:", 2)
# print("Masuk:", 1)
# print("selesai") 
# print("Keluar:", 1)
# print("Keluar:", 2)
# print("Keluar:", 3)
# n = 2 
# print("Masuk:", 2)
# print("Masuk:", 1)
# print("selesai") 
# print("Keluar:", 1)
# print("Keluar:", 2)
# n = 1
# print("Masuk:", 1)
# print("selesai") 
# print("Keluar:", 1)
# n = 0 
# print("selesai")