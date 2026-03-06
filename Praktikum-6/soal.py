def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i]<alist[i+1]: # Pengecekan apakah data pertama lebih besar dari data kedua
                exchanges = True
                temp = alist[i] # Simpan data pertama
                alist[i] = alist[i+1] # Posisi data pertama diganti dengan data kedua
                alist[i+1] = temp # Posisi data kedua diganti dengan data pertama
    passnum = passnum-1

data = [43,76,12,89,33,57,98, 22,68,9]
shortBubbleSort(data)
print(data)
# 1. Skor lima tertinggi
print(data[:5])
# 2. Kandidat yang lolos
# pertama, data index ke 6 yaitu : 98
# kedua, data index ke 4 yaitu : 89
# ketiga, data index ke 1 yaitu : 76
# keempat, data index ke 8 yaitu : 68
# kelima, data index ke 5 yaitu : 57
