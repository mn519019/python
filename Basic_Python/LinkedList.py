class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next =next

class LinkedList:
    def __init__(self, head = None):
        self.head = head # The root pointer
    
    def printlist(self): 
        temp = self.head 
        while temp: 
            if temp.next:
                print (temp.data, end = "-> ")
                temp = temp.next
            else:
                print(temp.data, end="\n")
                break
    
    def size(self):
        cur = self.head
        count = 0 
        while cur:
            count += 1
            cur = cur.next
        return print("Total Count: ",count)


list1 = LinkedList()
list1.head = Node(1)
s = Node(2)
t = Node(3)
list1.head.next = s
s.next = t

list1.printlist()
list1.size()
    
