#===========================================================================================
# Nama : Ihsan Hamizan
# NIM : J0403251051
# Kelas : A2 
#===========================================================================================


#===========================================================================================
# Implementasi Dasar : Queue
#===========================================================================================
    
class Node :
    # Konstruktor adakah fungsi yang dijalankan scara otomatis ketika class Node dipanggil / diinstantiasi 
    def __init__(self, data):
        self.data = data # Menyimpan nilai atau data pada list
        self.next = None # Pointer ini menunjuk ke note berikutnya (awal=none)

class queue :
    def __init__(self):
        self.front = None #Node paling depan
        self.rear = None #Node paling belakang

    def is_empty(self) :
        return self.front is None
    
    # membuat fungsi untuk menambahkan data baru
    def enquque(self, data) :
        nodeBaru = Node(data)

        if self.is_empty() :
            self.front = nodeBaru
            self.rear = nodeBaru
            return
        
        # jika queue tidak kosong, maka letakkan data baru setelah rear, dan jadikan data baru sebagai rear
        self.rear.next = nodeBaru #Letakkan data baru pada setelahnya rear
        self.rear = nodeBaru #Jadikan data baru sebagai user


    def dequque(self):
        if self.front is None :
            self.rear = None
            return

        #Menghapus data dari depan / front  
        data_terhapus = self.front.data #Lihat data paling depan

        #geser front ke node berikutnya 
        self.front = self.front.next

        #jika setelah geser front menjadi none, maka queue kosong
        #rear juga harus jadi none

        return data_terhapus
        

    def tampilkan(self) :
        current = self.front
        print("Front->",end=" ")
        while current is not None :
            print(current.data, end="-> " )
            current = current.next
        print("Rear")

q = queue()
q.enquque("A")
q.enquque("B")
q.enquque("C")
q.enquque("D")
q.enquque("E")
q.tampilkan()
q.dequque()
q.dequque()
q.dequque()
q.dequque()
q.dequque()
q.dequque()

q.tampilkan()