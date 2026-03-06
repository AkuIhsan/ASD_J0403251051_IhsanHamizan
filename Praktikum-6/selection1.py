#########################################
# Nama : Ihsan Hamizan 
# Nim : J0403251051
# Kelas : TPL A2
# SelectionSort Ascending
#########################################

def selectionSort(data):

    for fillslot in range(len(data)-1,0,-1):
        positionOfMax=0
        for location in range(1,fillslot+1):
            if data[location]>data[positionOfMax]:
                positionOfMax = location
        # Swap
        temp = data[fillslot]
        data[fillslot] = data[positionOfMax]
        data[positionOfMax] = temp


data = [21,13,14,27,1,83,65,22,4]
selectionSort(data)
print(data)

