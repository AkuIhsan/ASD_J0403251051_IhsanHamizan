#########################################
# Nama : Ihsan Hamizan 
# Nim : J0403251051
# Kelas : TPL A2
# BubleSort Ascending
#########################################


def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i]>alist[i+1]: # Pengecekan apakah data pertama lebih besar dari data kedua
                exchanges = True
                temp = alist[i] # Simpan data pertama
                alist[i] = alist[i+1] # Posisi data pertama diganti dengan data kedua
                alist[i+1] = temp # Posisi data kedua diganti dengan data pertama
    passnum = passnum-1

alist=[1,3,4,2,6,7,8,5,9,10]
shortBubbleSort(alist)
print(alist)
