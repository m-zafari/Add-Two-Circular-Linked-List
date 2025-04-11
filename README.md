the method of add_CLL(list1,list2) add together two circular linked list
# for example
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

--> 123 --> 11 --> 2 --> 56 --> 12 --> 5 --> 4 --> 3 --> 2 --> 1 -->
------<-------<-------<-------<------<------<-------<--------<------

output:
123 11 2 56 12 5 4 3 2 1 
