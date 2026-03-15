class Node:
        def __init__(self,data):
                self.data=data
                self.next_node=None
                
class LinkedList:
        def __init__(self) -> None:
                self.head=None
                self.size=0
                
        def insert(self,data):
                self.size+=1
                
                new_node=Node(data)
                
                if self.head == Node:
                        self.head = new_node
                else:
                        new_node.next_node = self.head
                        self.head = new_node
        def traverse_list(self):
                
                actual_node=self.head
                
                while actual_node is not None:
                        print('%d'% actual_node.data)
                        actual_node=actual_node.next_node
                        
        def get_middle_node(self):
                fast_pointer=self.head
                slow_pointer=self.head
                while fast_pointer.next_node and fast_pointer.next_node.next_node :
                        fast_pointer = fast_pointer.next_node.next_node
                        slow_pointer = slow_pointer.next_node
                        
                return slow_pointer
                        
                        
linked_list=LinkedList()
linked_list.insert(10)
linked_list.insert(20)
linked_list.insert(30)
linked_list.insert(40)
linked_list.insert(50)
linked_list.traverse_list()

print(linked_list.get_middle_node().data)