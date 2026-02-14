class Node :
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedlist :
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end(self, node) :
        if self.head == None :
            self.head = node
            self.tail = node
        else :
            nodeTemp = self.tail
            self.tail.next = node
            self.tail = node
            self.tail.prev = nodeTemp
        

    def display(self) :
        temp = self.head
        while temp.next != None :
            print(f"{temp.data}->", end="") 
            temp = temp.next
        else :
            print(f"{temp.data}->Null", end="") 

    def delete_node(self, node) :
        temp = self.head
        if node == self.head :
            nodeNext = node.next
            nodeNext.prev = None
            self.head = nodeNext
        elif node == self.tail :
            nodePrev = node.prev
            nodePrev.next = None
            self.tail = nodePrev
        else :
            while True :
                if temp == node :
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
                    break
                temp = temp.next

                


node1 = Node(5)
node2 = Node(6)
node3 = Node(7)

Linkedlist = DoublyLinkedlist()
Linkedlist.insert_at_end(node1)
Linkedlist.insert_at_end(node2)
Linkedlist.insert_at_end(node3)
Linkedlist.delete_node(node3)
Linkedlist.display()
