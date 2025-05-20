#!/usr/bin/python3
"""
Defines a Node of a singly linked list.
"""


class Node:
    """Represents a node in a singly linked list."""

    def __init__(self, data, next_node=None):
        """
        Initializes a new Node.

        Args:
            data: The data for the node.
            next_node: The next node, default is None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieves the data from the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the data for the node with type validation."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieves the next node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the next node, ensuring it's a Node or None."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


"""
Defines a Node class and SinglyLinkedList class with sorted insertion.
"""


class Node:
    """Represents a node in a singly linked list."""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list."""

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        new_node = Node(value)

        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        current = self.__head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        values = []
        current = self.__head
        while current:
            values.append(str(current.data))
            current = current.next_node
        return "\n".join(values)
