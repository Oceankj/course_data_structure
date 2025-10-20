import collections
from typing import Callable, Deque, Optional


class Node:
    def __init__(self, data: int):
        self.data = data
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


class HeapBuilder:
    def __init__(self, input: Optional[list[int]] = None):
        self.input: Optional[list[int]] = None

    def __build_binary_tree(self) -> Optional[Node]:
        if self.input is None:
            return None

        n = len(self.input)
        if n == 0:
            return None

        root = Node(self.input[0])
        i = 1
        q: Deque[Node] = collections.deque([root])

        while i < n:
            node = q.popleft()

            if i < n:
                newNode = Node(self.input[i])
                node.left = newNode
                q.append(newNode)
                i += 1

            if i < n:
                newNode = Node(self.input[i])
                node.right = newNode
                q.append(newNode)
                i += 1

        return root

    def __heapify(self, i: int, compare: Callable):
        if self.input is None:
            return None

        n = len(self.input)
        if 2 * i + 1 >= n:
            return

        selected_i = i
        left_i = 2 * i + 1
        right_i = 2 * i + 2

        if left_i < n and compare(
            self.input[left_i],
            self.input[selected_i],
        ):
            selected_i = left_i

        if right_i < n and compare(
            self.input[right_i],
            self.input[selected_i],
        ):
            selected_i = right_i

        if selected_i != i:
            self.input[i], self.input[selected_i] = (
                self.input[selected_i],
                self.input[i],
            )
            self.__heapify(selected_i, compare)

    def createMinHeap(self, input: list[int]) -> Optional[Node]:
        self.input = input
        n = len(self.input)
        for i in range(n // 2 - 1, -1, -1):
            self.__heapify(i, lambda a, b: a < b)
        return self.__build_binary_tree()

    def createMaxHeap(self, input: list[int]) -> Optional[Node]:
        self.input = input
        n = len(self.input)
        for i in range(n // 2 - 1, -1, -1):
            self.__heapify(i, lambda a, b: a > b)
        return self.__build_binary_tree()
