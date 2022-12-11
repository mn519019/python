# How to use a node and create a manual linked list
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

node = Node(6)
first = Node(3)
second = Node(4)
third = Node(2)
fourth = Node(1)
node.next = first
first.next = second
second.next = third
third.next = fourth

print(node.data,"->",first.data,"->",second.data
    ,"->",third.data,"->",fourth.data)
# Expected output 6 -> 3 -> 4 -> 2 -> 1
