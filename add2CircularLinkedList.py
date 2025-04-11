# Mohammad Zafari
# mhdzafari80@gmail.com

class Node: 
       
    def __init__(self, data = None): 
        self.data = data  
        self.next = None
  
class CircularLinkedList: 
      
    def __init__(self): 
        self.head = None 
    
    def push(self, data): 
        given_node = Node(data) 
        temp = self.head 
          
        given_node.next = self.head 
   
        if self.head is not None: 
            while(temp.next != self.head): 
                temp = temp.next 
            temp.next = given_node 
  
        else: 
            given_node.next = given_node 
  
        self.head = given_node 
    
    def print_CLL(self):
        node = self.head
        while True:
            print(f"{node.data}", end=" ")
            if node.next == self.head:
                break 
            node = node.next
        print()
    
    def add_CLL(list1,list2): 
        temp1 = list1.head
        temp2 = list2.head 
        if list1.head is not None:
            if list2.head is not None:
                while(temp1.next != list1.head): 
                    temp1 = temp1.next
                temp1.next = temp2
                while(temp2.next != list2.head):
                    temp2 = temp2.next
                temp2.next = list1.head
                return list1
            else:
                return list1
        else:
            if list2.head is not None:
                return list2
            else:
                return None  

  
"""
list1 = CircularLinkedList()  
list1.push(12) 
list1.push(56) 
list1.push(2) 
list1.push(11)
list1.push(123)

list2 = CircularLinkedList()  
list2.push(1) 
list2.push(2) 
list2.push(3) 
list2.push(4)
list2.push(5)

list3 = CircularLinkedList.add_CLL(list1,list2)
list3.print_CLL()
"""

# --> 123 --> 11 --> 2 --> 56 --> 12 --> 5 --> 4 --> 3 --> 2 --> 1 -->
# ------<-------<-------<-------<------<------<-------<--------<------