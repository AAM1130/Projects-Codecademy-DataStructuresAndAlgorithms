#
# Created by SituationUnknown(AAM1130) on 8/26/25
#
# Sample Python implementation of a doubly linked list.
#

from __future__ import annotations # requires Python 3.7+ for type hinting Node class inside Node class init method


# Node class to act as nodes in the linked list
class Node:
    # In this example the Node value is limited to an integer.
    def __init__(self, value: int, next_node: Node | None=None, prev_node: Node | None=None)-> None:
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node

    # setter method for next node
    def set_next_node(self, next_node: Node | None) -> None:
        self.next_node = next_node

    # getter method for next node
    def get_next_node(self)-> Node | None:
        return self.next_node

    # setter method for previous node
    def set_prev_node(self, prev_node: Node | None) -> None:
        self.prev_node = prev_node

    # getter method for previous node
    def get_prev_node(self)-> Node | None:
        return self.prev_node

    # getter method for node stored value
    def get_value(self)-> int:
        return self.value


# Doubly linked list class
class DoublyLinkedList:
    # class is initialized with empty head and tail nodes.
    head_node: Node | None
    tail_node: Node | None

    def __init__(self)-> None:
        self.head_node = None
        self.tail_node = None

    # method to add a new node to the head position.
    def add_to_head(self, new_value: int) -> None:
        new_head = Node(new_value)
        current_head = self.head_node

        if current_head is not None:
            current_head.set_prev_node(new_head)
            new_head.set_next_node(current_head)

        self.head_node = new_head

        if self.tail_node is None:
            self.tail_node = new_head

    # method to add a new node to the tail position
    def add_to_tail(self, new_value: int) -> None:
        new_tail = Node(new_value)
        current_tail = self.tail_node

        if current_tail is not None:
            current_tail.set_next_node(new_tail)
            new_tail.set_prev_node(current_tail)

        self.tail_node = new_tail

        if self.head_node is None:
            self.head_node = new_tail

    # method to remove the current head node
    def remove_head(self)-> int | None:
        removed_head = self.head_node

        if removed_head is None:
            return None

        self.head_node = removed_head.get_next_node()

        if self.head_node is not None:
            self.head_node.set_prev_node(None)

        if removed_head == self.tail_node:
            self.remove_tail()

        return removed_head.get_value()

    # method to remove the current tail node
    def remove_tail(self)-> int | None:
        removed_tail = self.tail_node

        if removed_tail is None:
            return None

        self.tail_node = removed_tail.get_prev_node()

        if self.tail_node is not None:
            self.tail_node.set_next_node(None)

        if removed_tail == self.head_node:
            self.remove_head()

        return removed_tail.get_value()

    # method to remove by Node value
    def remove_by_value(self, value_to_remove: int)-> Node | None:
        node_to_remove = None
        current_node = self.head_node

        while current_node is not None:
            if current_node.get_value() == value_to_remove:
                node_to_remove = current_node
                break

            current_node = current_node.get_next_node()

        if node_to_remove is None:
            return None

        if node_to_remove == self.head_node:
            self.remove_head()
        elif node_to_remove == self.tail_node:
            self.remove_tail()
        else:
            next_node = node_to_remove.get_next_node()
            prev_node = node_to_remove.get_prev_node()
            next_node.set_prev_node(prev_node)
            prev_node.set_next_node(next_node)

        return node_to_remove

    # method to return the current linked list as string.
    def stringify_list(self)-> str | None:
        string_list = ""
        current_node = self.head_node

        while current_node:

            if current_node.get_next_node() is not None:
                string_list += str(current_node.get_value()) + "\n"

            current_node = current_node.get_next_node()

        return string_list


# functional example
if __name__ == '__main__':

    # create doubly linked list
    dll = DoublyLinkedList()

    # add a few nodes to the list
    for i in range(0, 20, 2):
        dll.add_to_tail(i)

    # view current linked list
    print(dll.stringify_list())     # should output even numbers 0, 2, 4, 6, 8, 10, 12, 14, 16

    # remove nodes with values 0 and 10
    dll.remove_head()
    dll.remove_by_value(10)

    # view modified linked list
    print(dll.stringify_list())


