#
# Created by SituationUnknown(AAM1130) on 11/13/25
#
# Sample Python implementation of the queue data structure.
#
"""
queue.py

A generic implementation of a queue data structure in Python.

This module defines a single class:
- Queue(Generic[T]):

Features:
- Type-safe with Python generics (TypeVar T)
- Education example block under '__main__' for demonstration and testing.

Designed for modular reuse and integration with static type checkers like mypy.
"""

from node import Node
from typing import TypeVar, Generic


T = TypeVar('T')

class Queue(Generic[T]):
    """
    A generic implementation of a queue data structure.

    """
    def __init__(self, max_size: int | None =None) -> None:
        """
        Initialization method for a queue data structure.
        :param max_size: int, max size of queue, or None for unlimited.
        """
        self.head: Node[T] | None = None
        self.tail: Node[T] | None = None
        self.max_size: int | None = max_size
        self.size: int = 0

    def enqueue(self, value: T) -> None:
        """
        Add a new node containing the given value to the queue.
        :param value: The value to be added to the queue. Should be of a consistent type.
        :raises OverflowError: If queue is full when attempting to call .enqueue()
        """
        if not self.has_space():
            raise OverflowError("Queue is full")

        new_node = Node(value)

        if self.is_empty():
            self.head = self.tail = new_node

        else:
            assert self.tail is not None, "Queue invariant violated: non-empty queue must have a tail."
            self.tail.set_next_node(new_node)
            self.tail = new_node

        self.size += 1

    def dequeue(self) -> T:
        """
        Remove the front node from the front of the queue and return the value.
        :raises IndexError: if queue is empty when attempting to dequeue.
        """
        if self.size == 0:
            raise IndexError("Dequeue attempt from empty queue.")

        assert self.head is not None, "Queue invariant violated: non-empty queue must have a head."
        item_to_remove = self.head

        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.get_next_node()

        self.size -= 1
        return item_to_remove.get_value()

    def peek(self) -> T | None:
        """
        Return the value stored at the head of the queue without removing it.
        :return: stored value or None if queue is empty
        """
        if self.size == 0:
            return None
        assert self.head is not None, "Queue invariant violated: non-empty queue must have a head."
        return self.head.get_value()

    def has_space(self) -> bool:
        """
        A helper method to check if there is space in the queue.
        :return: bool
        """
        if self.max_size is None:
            return True
        else:
            return self.max_size > self.size

    def is_empty(self) -> bool:
        """
        A helper method to check if the queue is empty.
        :return: bool
        """
        return self.size == 0


if __name__ == "__main__":
    message_buffer: Queue[str] = Queue(max_size=5)
    message_list = ['Alpha', 'Beta', 'Gamma', 'Delta', 'Epsilon']

    for message in message_list:
        message_buffer.enqueue(message)

    print(message_buffer.size)
    print(message_buffer.peek())

    # attempt overflow
    try:
        message_buffer.enqueue('Zeta')
    except OverflowError as e:
        print(f"Error: {e}")

    while not message_buffer.is_empty():
        print(message_buffer.dequeue())
