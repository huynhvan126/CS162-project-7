# Author: Van Huynh
# GitHub username: huynhvan126
# Date: 11/06/2024
# Description: Write a LinkedList that has recursive implementations of the add, remove, contains, insert, and reverse methods.
class Node:
    def __init__(self, data):
        """Initialize a node with data and pointer to its next node, set to None."""
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        """Initialize an empty linked list."""
        self._head = None

    def get_head(self):
        """Return the node's head of the linked list."""
        return self._head

    def rec_add(self, a_node, data):
        """Recursively add a node to the linked list."""
        if a_node.next is None:
            a_node.next = Node(data)
        else:
            self.rec_add(a_node.next, data)

    def add(self, data):
        """Add a node to the end of the linked list."""
        if self._head is None:
            self._head = Node(data)
        else:
            self.rec_add(self._head, data)

    def rec_remove(self, a_node, data):
        """Recursively remove a node from the linked list."""
        if a_node.next is None or a_node.next is None:
            return
        if a_node.next.data == data:
            a_node.next = a_node.next.next
        else:
            self.rec_remove(a_node.next, data)

    def remove(self, data):
        """Remove the first occurrence of the specified data."""
        if self._head is None:
            return
        if self._head.data == data:
            self._head = self._head.next
        else:
            self.rec_remove(self._head, data)

    def rec_contains(self, a_node, data):
        """Recursively check if a node is present in the linked list."""
        if a_node is None:
            return False
        if a_node.data == data:
            return True
        return self.rec_contains(a_node.next, data)

    def contains(self, data):
        """Check if the linked list is contained in the specified data."""
        return self.rec_contains(self._head, data)

    def rec_insert(self, a_node, index, data):
        """Recursively insert a node to the linked list."""
        if index == 1:
            new_node = Node(data)
            new_node.next = a_node.next
            a_node.next = new_node
        else:
            self.rec_insert(a_node.next, index - 1, data)

    def insert(self, data, index):
        """Insert an element at the specified index in the linked list."""
        if index == 0:
            new_node = Node(data)
            new_node.next = self._head
            self._head = new_node
        else:
            self.rec_insert(self._head, index, data)

    def rec_reverse(self, current, prev=None):
        """Recursively reverse the linked list."""
        if current is None:
            self._head = prev
            return
        next_node = current.next
        current.next = prev
        self.rec_reverse(next_node, current)

    def reverse(self):
        """Reverse the linked list."""
        self.rec_reverse(self._head)

    def rec_to_plain_list(self, a_node, result):
        """Recursively convert a linked list to a plain list."""
        if a_node is None:
            return result
        result.append(a_node.data)
        return self.rec_to_plain_list(a_node.next, result)

    def to_plain_list(self):
        """Convert a list of the linked list."""
        return self.rec_to_plain_list(self._head, [])

    def rec_display(self, a_node):
        """Recursive display method for printing linked list elements."""
        if a_node is None:
            return
        print(a_node.data, end=" ")
        self.rec_display(a_node.next)

    def display(self):
        """Helper method to display linked list."""
        self.rec_display(self._head)
        print()
