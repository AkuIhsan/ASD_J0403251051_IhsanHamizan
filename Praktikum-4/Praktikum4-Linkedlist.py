#===========================================================================================
# Nama : Ihsan Hamizan
# NIM : J0403251051
# Kelas : A2 
#===========================================================================================


#===========================================================================================
# Implementasi Dasar : Node pada Linked List
#===========================================================================================

class Node :
    # Konstruktor adakah fungsi yang dijalankan scara otomatis ketika class Node dipanggil / diinstantiasi 
    def __init__(self, data):
        self.data = data # Menyimpan nilai atau data pada list
        self.next = None # Pointer ini menunjuk ke note berikutnya (awal=none)

#1) membuat node dengan instantiasi class node
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")

#2) mendefinisikan head dan Menghubungkan Node : A->B->C->None
head = nodeA
nodeA.next = nodeB
nodeB.next = nodeC

#3) Traversal : Menelusuri node dari head sampai ke None
current = head
while current is not None :
    print(current.data) # Menampilkan data pada node saat ini
    current = current.next # Pindah ke node berikutnya
