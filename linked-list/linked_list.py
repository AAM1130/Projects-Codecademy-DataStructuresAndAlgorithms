#
# Created by SituationUnknown(AAM1130) on 11/11/25
#
# Sample Python implementation of a linked list using TypeVar and Generic.
#

from __future__ import annotations  # requires Python 3.7+ for type hinting Node class inside Node class init method
from typing import TypeVar, Generic  # requires Python 3.10+ for full functionality

T = TypeVar('T')  # T can be any type


# Node class to act as nodes in the linked list
class Node(Generic[T]):
    # In this example the Node value can store 'Any' data of a common type
    def __init__(self, value: T, next_node: Node[T] | None = None) -> None:
        self.value = value
        self.next_node = next_node

    #Example usage: string_node = Node[str]('hello')

    # setter method for next node
    def set_next_node(self, next_node: Node[T] | None) -> None:
        self.next_node = next_node

    # getter method for next node
    def get_next_node(self) -> Node[T] | None:
        return self.next_node

    # getter method for node stored value
    def get_value(self) -> T:
        return self.value


# Singly linked list class
class LinkedList(Generic[T]):
    # Class initialized with empty head node
    def __init__(self) -> None:
        self.head_node: Node[T] | None = None

    # method to add a new node to the head position.
    def add_to_head(self, new_value: T) -> None:
        new_head = Node(new_value)
        current_head = self.head_node

        if current_head is not None:
            new_head.set_next_node(current_head)

        self.head_node = new_head

    # method to add a new node to the tail position
    def add_to_tail(self, new_value: T) -> None:
        if self.head_node is None:
            self.head_node = Node(new_value)

        current = self.head_node
        while current.get_next_node() is not None:
            next_node = current.get_next_node()
            if next_node is None:
                break
            current = next_node

        current.set_next_node(Node(new_value))

    # method to remove the current head node
    def remove_head(self) -> T | None:
        removed_head = self.head_node

        if removed_head is None:
            return None

        self.head_node = removed_head.get_next_node()
        return removed_head.get_value()

    # method to remove a node from the list based on its current value
    def remove_by_value(self, value_to_remove: T) -> T | None:
        current_node = self.head_node

        # Case 1: Head node is the one to remove
        if current_node is not None and current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
            return current_node.get_value()

        # Case 2: Search for the node to remove
        while current_node is not None:
            next_node = current_node.get_next_node()
            if next_node is None:
                break
            if next_node.get_value() == value_to_remove:
                current_node.set_next_node(next_node.get_next_node())
                return next_node.get_value()
            current_node = next_node

        # Case 3: Value not found
        return None

    # method to return the current linked list as string.
    def stringify_list(self)-> str | None:
        string_list = ""
        current_node = self.head_node

        while current_node:

            string_list += str(current_node.get_value()) + "\n"
            current_node = current_node.get_next_node()

        return string_list


# functional example
if __name__ == '__main__':
    # create a new list of str types
    my_state_list: LinkedList[str] = LinkedList()

    # add states that I have been in
    my_state_list.add_to_head('Ohio')
    my_state_list.add_to_tail('South Carolina')
    my_state_list.add_to_tail('Connecticut')
    my_state_list.add_to_tail('Florida')

    # add states that would be fun to visit
    my_state_list.add_to_tail('Alaska')
    my_state_list.add_to_tail('Arizona')
    my_state_list.add_to_tail('Washington')

    # try to add some junk to see if the type checker flags
    # my_state_list.add_to_head(13.0123)
    # my_state_list.add_to_tail(46)

    # output list
    print(20 * '-')
    print(my_state_list.stringify_list())
    print(20 * '-')
    my_state_list.remove_by_value('Arizona')
    print(my_state_list.stringify_list())
    print(20 * '-')
