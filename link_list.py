class Node:
    def __init__(self, data):
        self.data = data
        self.next = None




class Linked_list:
    def __init__(self):
        self.head = None
    
    def insertAtStart(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    # def insertAtEnd(self, data):
    #     curr = self.head
    #     node = Node(data)
    #     if curr is None:
    #         self.head = node

    #     else:
    #         while curr.next is not None:
    #             curr = curr.next
    #         curr.next = node

    def __str__(self):
        linklist = ""
        curr = self.head
        while curr is not None:
            linklist += f"{curr.data}|"
            curr = curr.next
        return linklist[:-1]
            

l = Linked_list()

l.insertAtStart(10)
l.insertAtStart(20)
l.insertAtStart(30)
l.insertAtStart(40)
l.insertAtStart(50)
l.insertAtStart(60)
l.insertAtStart(70)
l.insertAtStart(80)

# print(l)



class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None

        
        
        
class Link:
    
    def __init__(self):
        self.head = None
    
    def insertstart(self,data):
        node = Node(data)
        node.next = self.head
        self.head = node
    
    def __str__(self):
        curr = self.head
        str2 = ""
        while curr is not None:
            str2 += f" {curr.data} "
            curr = curr.next
            
        return str2

p = Link()

p.insertstart(10)   
p.insertstart(20)
p.insertstart(30)
p.insertstart(40)

            


