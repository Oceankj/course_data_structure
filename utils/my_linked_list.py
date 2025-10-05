from typing import Any, Generic, TypeVar, Optional

T = TypeVar("T")


class MyNode(Generic[T]):
    def __init__(self, value: Optional[T] = None):
        self.value: Optional[T] = value
        self.next = None
        self.prev = None


class MyLinkedList:
    def __init__(self):
        self.__head = MyNode()
        self.__tail = MyNode()
        self.__head.next = self.__tail
        self.__tail.prev = self.__head
        self.__size = 0

    def add_before(self, node: MyNode, new_node: MyNode):
        if node.prev is None:
            raise ValueError("cannot insert before head")
        node.prev.next = new_node
        new_node.prev = node.prev
        new_node.next = node
        node.prev = new_node
        self.__size += 1

    def add_after(self, node: MyNode, new_node: MyNode):
        if node.next is None:
            raise ValueError("cannot insert after tail")
        node.next.prev = new_node
        new_node.next = node.next
        new_node.prev = node
        node.next = new_node
        self.__size += 1

    def add_first(self, value: Any):
        new_node = MyNode[Any](value)
        self.add_after(self.__head, new_node)

    def add_last(self, value: Any):
        new_node = MyNode[Any](value)
        self.add_before(self.__tail, new_node)

    def delete_node(self, node: MyNode):
        if node.prev is None or node.next is None:
            raise ValueError("node is not properly linked")
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None
        self.__size -= 1

    def get_last_node(self) -> MyNode:
        if self.is_empty():
            raise ValueError("list is empty")
        return self.__tail.prev

    def get_first_node(self) -> MyNode:
        if self.is_empty():
            raise ValueError("list is empty")
        return self.__head.next

    def size(self):
        return self.__size

    def is_empty(self):
        return self.__size == 0
