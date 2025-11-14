#
# Created by SituationUnknown(AAM1130) on 11/13/25
#
# Sample Python implementation of the queue data structure.
#
"""
node.py

A generic implementation of a Node container in Python for various data structures.

This module defines a single class:
- Node[T]: a node in a data structure.

Features:
- Type-safe with Python generics (TypeVar T)
- Education example block under '__main__' for demonstration and testing.

Designed for modular reuse and integration with static type checkers like mypy.
"""

from __future__ import annotations  # requires Python 3.7+ for type hinting Node class inside Node class init method
from typing import TypeVar, Generic  # requires Python 3.10+ for full functionality and union type syntax

T = TypeVar('T')  # T can be any type

class Node(Generic[T]):
    """
    A generic node implementation for data structures.
    """
    def __init__(self, value: T , next_node: Node[T] | None = None) -> None:
        """
        Initializes a new Node instance.
        :param value: The data to be stored in the node.
        :param next_node: The next node pointer of this node, or None
        """
        self.value = value
        self.next_node = next_node

    # Example usage: string_node = Node[str]('hello')

    # setter method for next node
    def set_next_node(self, next_node: Node[T] | None) -> None:
        """
        Sets the next node in the structure.
        :param next_node: The next node pointer of this node
        """
        self.next_node = next_node

    # getter method for next node
    def get_next_node(self) -> Node[T] | None:
        """
        Returns the next node in the structure.
        :return: Returns the next node parameter of this node or None
        """
        return self.next_node

    # getter method for node stored value
    def get_value(self) -> T:
        """
        Returns the data stored in the node.
        :return: Returns the data stored in the node.
        """
        return self.value


if __name__ == '__main__':
    node_a = Node[int](13)
    node_b = Node[int](99, node_a)
    print(node_b.get_value())         # 99
    print(node_b.get_next_node())     # Node object at ........
