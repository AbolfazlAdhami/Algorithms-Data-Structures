from typing import Optional


class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.next_node: Optional[Node] = None


class LinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.size = 0

    def insert(self, data: int) -> None:
        new_node = Node(data)


        if self.head is None:
            self.head = new_node
        else:

            new_node.next_node = self.head
            self.head = new_node
        self.size += 1

    def traverse_list(self) -> None:
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next_node

    def get_middle_node(self) -> Optional[Node]:
        slow_pointer = self.head
        fast_pointer = self.head


        while fast_pointer is not None and fast_pointer.next_node is not None:
            fast_pointer = fast_pointer.next_node.next_node
            slow_pointer = slow_pointer.next_node

        return slow_pointer


linked_list = LinkedList()
for value in [10, 20, 30, 40, 50]:
    linked_list.insert(value)


linked_list.traverse_list()

middle = linked_list.get_middle_node()
if middle is not None:
    print("Middle Index: ", middle.data)
else:
    print("List is Empty")
