from typing import Any
from utils import MyLinkedList


class Stack:
    def __init__(self):
        self.__list = MyLinkedList()

    def push(self, e: Any) -> None:
        self.__list.add_last(e)

    def pop(self) -> Any:
        try:
            node = self.__list.get_last_node()
        except ValueError:
            raise ValueError("node is not exist")

        self.__list.delete_node(node)
        return node.value

    def peek(self) -> Any:
        try:
            node = self.__list.get_last_node()
        except ValueError:
            raise ValueError("node is not exist")

        return node.value

    def size(self):
        return self.__list.size()
