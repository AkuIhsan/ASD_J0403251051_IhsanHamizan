# ==========================================================
# Contoh Rekursi 3: Menjumlahkan Elemen List
# Nama : IHSAN HAMIZAN
# Nim : J0403251051
# Kelas : TPL A2
# ==========================================================
def jumlah_list(data, index=0):
    # Base case: jika index sudah mencapai panjang list
    if index == len(data):
        return 0
    
    # Recursive case: elemen sekarang + jumlah elemen setelahnya
    return data[index] + jumlah_list(data, index + 1)

print(jumlah_list([7, 8, 9, 10])) # Output: 34