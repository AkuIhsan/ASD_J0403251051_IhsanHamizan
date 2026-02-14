class Node :
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedlist :
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end(self, data) :
        new_node = Node(data=data)
        if self.head == None :
            self.head = new_node
            self.tail = new_node
        else :
            nodeTemp = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.tail.prev = nodeTemp

    def display(self) :
        temp = self.head
        while True :
            if temp == self.tail :
                print(f"Node dengan data {temp.data}")
                break
            print(f"Node dengan data {temp.data}")
            temp = temp.next
    
    def search(self,num) :
        if self.head == None :
            print(f"DoublyLinkedlist kosong, Tidak ada elemen yang bisa dicari")
            return
        
        temp = self.head
        while True :
            if temp.data == num :
                print(f"Elemen {num} di temukan")
                break
            if temp == self.tail :
                print("Elemen tidak ditemukan")
                break
            temp = temp.next

list = DoublyLinkedlist()
list.insert_at_end(1)
list.insert_at_end(2)
list.insert_at_end(3)
list.insert_at_end(4)
list.insert_at_end(5)
list.display()
list.search(6)