from typing import Any
from utils.my_linked_list import MyLinkedList


class Queue:

    def __init__(self) -> None:
        self.__list = MyLinkedList()

    def enqueue(self, value: Any) -> None:
        self.__list.add_last(value)

    def dequeue(self) -> Any:
        node = self.__list.get_first_node()
        self.__list.delete_node(node)
        return node.value

    def poll(self) -> Any:
        return self.__list.get_first_node().value

    def size(self) -> int:
        return self.__list.size()
