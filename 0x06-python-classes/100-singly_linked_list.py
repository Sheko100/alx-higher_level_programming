#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Class Node

    Creates a singly linked list
"""


class Node:
    """Defines a node of a singly linked list

    Args:
        data (int): data to store
        next_node: Node object
    """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """int: integer number to add to the Node"""
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """Node: an instance of the Node class"""

        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__data = value
            

class SinglyLinkedList:
    """defines a singly linked list

    Args:
        head (Node): a linked list head
    """
    def __init__(self):
        self.__head = None
        if (self.__head is not None):
            print(self.__head)

    def sorted_insert(self, value):
        """inserts a Node in a singly linked list in ascending order

        Args:
            value (int): integer to add to the Node
        """
        head = self.__head
        if head is not None:
            node = head
            while (node is not None and node.data < value):
                currnode = node
                node = node.next_node
            currnode.next_node = newnode
            newnode = Node(value, node)
        else:
            head = Node(value)
