class node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = node()
    
    def append(self,data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node
        
        
    def length(self):
        tot = 0
        cur = self.head
        while cur.next !=None:
            tot += 1
            cur = cur.next
        return tot
    
    def display(self):
        arr = []
        cur = self.head
        while cur.next !=None:
            arr.append(cur.next.data)
            cur = cur.next
        print(arr)
        
myList = LinkedList()
print(myList.length())

myList.append(50)
myList.append(51)
myList.display()

        
            
        
        