class Node :
    def __init__(self,data):
        self.data = data
        self.next = None

class SingleLinkedList :
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end(self, data) :
        new_node = Node(data)
        if self.head == None :
            self.head = new_node
            self.tail = new_node
        else :
            self.tail.next = new_node
            self.tail = new_node

    def display(self) :
        temp = self.head
        while True :
            if temp.next == None :
                print(f"{temp.data}->null")
                break
            print(f"{temp.data}->",end="")
            temp = temp.next
    
    def reverse(self) :
        listNode = []
        temp = self.head
        while True :
            if temp.next == None :
                break
            listNode.append(temp)
            temp = temp.next

        self.head = self.tail
        temp = self.head
        for i in range(-1,(-1*len(listNode)-1),-1) :
            if i == (-1*len(listNode)) :
                self.tail = listNode[i]
                self.tail.next = None
                listNode[i+1].next = self.tail
                break
            temp.next = listNode[i]
            temp = listNode[i]



        


sll = SingleLinkedList()
sll.insert_at_end(1)
sll.insert_at_end(2)
sll.insert_at_end(3)
sll.insert_at_end(4)
sll.insert_at_end(5)
sll.display()
sll.reverse()
sll.tes()
sll.display()