from typing import Any
from ..utils import MyLinkedList


class Stack:
    def __init__(self):
        self.s = MyLinkedList()

    def push(self, e: Any) -> None:
        self.s.add_last(e)

    def pop(self) -> Any:
        try:
            node = self.s.get_last_node()
        except ValueError:
            raise ValueError("node is not exist")

        self.s.delete_node(node)
        return node.value

    def peek(self) -> Any:
        try:
            node = self.s.get_last_node()
        except ValueError:
            raise ValueError("node is not exist")

        return node.value

    def size(self):
        return self.s.size()
