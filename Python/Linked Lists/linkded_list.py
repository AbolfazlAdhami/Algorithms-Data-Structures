from __future__ import annotations
from typing import Optional


class Node:
    next_node: Optional['Node']

    def __init__(self, data: int):
        self.data = data
        self.next_node = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
        self.size += 1

    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next_node:
                current = current.next_node
            current.next_node = new_node
        self.size += 1

    def remove(self, data):
        if self.head is None:
            return False
        # Remove head
        if self.head.data == data:
            self.head = self.head.next_node
            self.size -= 1
            return True
        # Remove non-head
        prev = self.head
        current = self.head.next_node
        while current:
            if current.data == data:
                prev.next_node = current.next_node
                self.size -= 1
                return True
            prev = current
            current = current.next_node
        return False

    def search(self, data):
        current = self.head
        index = 0
        while current:
            if current.data == data:
                return index
            current = current.next_node
            index += 1
        return -1

    def traverse(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next_node
        return elements

    def get_middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next_node:
            slow = slow.next_node
            fast = fast.next_node.next_node
        return slow.data if slow else None


def main():
    ll = LinkedList()

    while True:
        print("\nChoose an operation:")
        print("1. Insert at head")
        print("2. Insert at tail")
        print("3. Remove a value")
        print("4. Search for a value")
        print("5. Display list")
        print("6. Get middle element")
        print("7. Display size")
        print("8. Exit")
        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            data = int(input("Enter an integer to insert at head: "))
            ll.insert_at_head(data)
            print(f"{data} has been inserted at the head.")
        elif choice == '2':
            data = int(input("Enter an integer to insert at tail: "))
            ll.insert_at_tail(data)
            print(f"{data} has been inserted at the tail.")
        elif choice == '3':
            data = int(input("Enter the integer to remove: "))
            if ll.remove(data):
                print(f"{data} was removed from the list.")
            else:
                print(f"{data} not found in the list.")
        elif choice == '4':
            data = int(input("Enter the integer to search for: "))
            pos = ll.search(data)
            if pos != -1:
                print(f"{data} found at position {pos}.")
            else:
                print(f"{data} not found in the list.")
        elif choice == '5':
            elements = ll.traverse()
            print("Current list:", elements)
        elif choice == '6':
            mid = ll.get_middle()
            if mid is not None:
                print(f"The middle element is: {mid}")
            else:
                print("The list is empty.")
        elif choice == '7':
            print(f"Current size of the list: {ll.size}")
        elif choice == '8':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")


if __name__ == "__main__":
    main()
