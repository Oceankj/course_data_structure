from typing import Callable, Optional
from swe_240p_data_structure.module4.BST import Node


class BSTToHeapTransformer:

    def __heapify(
        self, root: Optional[Node], compare: Callable
    ) -> Optional[Node]:
        if root is None:
            return None
        left = self.__heapify(root.left, compare)
        right = self.__heapify(root.right, compare)

        selected_node: Node = root
        if left is not None and compare(
            left.data["last_name"], selected_node.data["last_name"]
        ):
            selected_node = left
        if right is not None and compare(
            right.data["last_name"], selected_node.data["last_name"]
        ):
            selected_node = right

        if selected_node != root:
            root.data, selected_node.data = selected_node.data, root.data
            self.__heapify(selected_node, compare)

        return root

    def bstToMinHeap(self, node: Optional[Node]) -> Optional[Node]:
        return self.__heapify(node, lambda a, b: a < b)

    def bstToMaxHeap(self, node: Optional[Node]) -> Optional[Node]:
        return self.__heapify(node, lambda a, b: a > b)
