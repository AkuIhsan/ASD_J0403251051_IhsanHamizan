#===========================================================================================
# Nama : Ihsan Hamizan
# NIM : J0403251051
# Kelas : A2 
#===========================================================================================


#===========================================================================================
# Implementasi Dasar : Stack
#===========================================================================================

class Node :
    # Konstruktor adakah fungsi yang dijalankan scara otomatis ketika class Node dipanggil / diinstantiasi 
    def __init__(self, data):
        self.data = data # Menyimpan nilai atau data pada list
        self.next = None # Pointer ini menunjuk ke note berikutnya (awal=none)

# Stack ada operasi push (Memasukkan head baru) dan pop (Menghapus head)

class Stack :
    def __init__(self):
        self.top = None #top menuju ke node paling atas (awalnya kosong)
    
    def is_empty(self) :
        return self.top is None # stack kosong jika top kosong
    
    def push(self, data) :
        #1 membuat node baru
        nodeBaru = Node(data) #instantiasi/memanggil konstruktor pada class Node 

        #2 node baru menunjuk ke top yang Lama (head lama)
        nodeBaru.next = self.top

        #3 Geser top pindah ke node baru
        self.top = nodeBaru

    def pop(self) : # Mengambil / menghapus node paling atas (top/head)
        if self.is_empty() :
            print("Stack kosong tidak bisa pop")
            return None
        data_terhapus = self.top.data # soroti bagian top dan disimpan di variabel
        self.top = self.top.next # Geser top ke node berikutnya
        return data_terhapus

    def peek(self) :
        # melihat data yang paling atas tanpa menghapus
        if self.is_empty() :
            return None
        return self.top.data



    def tampilkan(self) :
        current = self.top
        print("Top", end="->")
        while current is not None :
            print(current.data, end="->")
            current = current.next
        print("None")

#Instantiasi Class Stack
s = Stack()
s.push("A")
s.push("B")
s.push("C")
s.pop()
s.tampilkan()
    