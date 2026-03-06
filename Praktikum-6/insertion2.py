#########################################
# Nama : Ihsan Hamizan 
# Nim : J0403251051
# Kelas : TPL A2
# InsertionSort Descending
#########################################

def insertionSort(data):
    for index in range(1,len(data)):
        currentvalue = data[index]
        position = index
        while position>0 and data[position-1]<currentvalue: # Ubah posisi yang tadi awalnya data[position-1]>current value menjadi "<"
            data[position] = data[position-1]
            position = position-1
            data[position] = currentvalue

data = [54,26,93,17,77,31,44,55,20]
insertionSort(data)
print(data)