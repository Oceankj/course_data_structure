from typing import Optional

import pytest
from swe_240p_data_structure.module4.BST import BST
from swe_240p_data_structure.module5.BST_to_heap_transformer import (
    BSTToHeapTransformer,
)
from swe_240p_data_structure.module5.heap_builder import HeapBuilder, Node


class TestTask1:

    def __is_min_heap(self, node: Optional[Node]):
        if node is None:
            return True
        valid = True
        if node.left:
            valid &= node.data <= node.left.data
            valid &= self.__is_min_heap(node.left)
        if node.right:
            valid &= node.data <= node.right.data
            valid &= self.__is_min_heap(node.right)
        return valid

    def __is_max_heap(self, node: Optional[Node]):
        if node is None:
            return True
        valid = True
        if node.left:
            valid &= node.data >= node.left.data
            valid &= self.__is_max_heap(node.left)
        if node.right:
            valid &= node.data >= node.right.data
            valid &= self.__is_max_heap(node.right)
        return valid

    def test_create_min_heap(self):
        arr = [5, 3, 8, 1, 2, 10]
        hb = HeapBuilder()
        root = hb.createMinHeap(arr.copy())

        assert root.data == min(arr)
        assert self.__is_min_heap(root)

    def test_create_max_heap(self):
        arr = [5, 3, 8, 1, 2, 10]
        hb = HeapBuilder()
        root = hb.createMaxHeap(arr.copy())

        assert root.data == max(arr)

        assert self.__is_max_heap(root)

    def test_empty_input(self):
        hb = HeapBuilder()
        assert hb.createMinHeap([]) is None
        assert hb.createMaxHeap([]) is None

    def test_single_element(self):
        hb = HeapBuilder()
        root_min = hb.createMinHeap([42])
        root_max = hb.createMaxHeap([42])
        assert root_min is not None and root_min.data == 42
        assert root_max is not None and root_max.data == 42
        assert root_min.left is None and root_min.right is None
        assert root_max.left is None and root_max.right is None

    def test_heapify_does_not_modify_sorted_min_heap(self):
        arr = [1, 2, 3, 4, 5]
        hb = HeapBuilder()
        root = hb.createMinHeap(arr.copy())

        assert self.__is_min_heap(root)

    def test_heapify_does_not_modify_sorted_max_heap(self):
        arr = [5, 4, 3, 2, 1]
        hb = HeapBuilder()
        root = hb.createMaxHeap(arr.copy())

        assert self.__is_max_heap(root)


class TestTask2:
    @pytest.fixture(autouse=True)
    def setUp(self):
        self.bst = BST()
        self.root = self.bst.root

    def __is_min_heap(self, node):
        if not node:
            return True
        valid = True
        if node.left:
            valid &= node.data["last_name"] <= node.left.data["last_name"]
            valid &= self.__is_min_heap(node.left)
        if node.right:
            valid &= node.data["last_name"] <= node.right.data["last_name"]
            valid &= self.__is_min_heap(node.right)
        return valid

    def __is_max_heap(self, node):
        if not node:
            return True
        valid = True
        if node.left:
            valid &= node.data["last_name"] >= node.left.data["last_name"]
            valid &= self.__is_max_heap(node.left)
        if node.right:
            valid &= node.data["last_name"] >= node.right.data["last_name"]
            valid &= self.__is_max_heap(node.right)
        return valid

    def test_bst_to_min_heap(self):
        transformer = BSTToHeapTransformer()
        min_heap_root = transformer.bstToMinHeap(self.root)
        assert self.__is_min_heap(min_heap_root)

    def test_bst_to_max_heap(self):
        transformer = BSTToHeapTransformer()
        max_heap_root = transformer.bstToMaxHeap(self.root)
        assert self.__is_max_heap(max_heap_root)

    def test_min_heap_order_preserves_elements(self):
        transformer = BSTToHeapTransformer()

        def collect_names(node):
            if not node:
                return []
            return (
                [node.data["last_name"]]
                + collect_names(node.left)
                + collect_names(node.right)
            )

        original_names = sorted(collect_names(self.root))
        min_heap_root = transformer.bstToMinHeap(self.root)
        heap_names = sorted(collect_names(min_heap_root))
        assert original_names == heap_names

    def test_max_heap_order_preserves_elements(self):
        transformer = BSTToHeapTransformer()

        def collect_names(node):
            if not node:
                return []
            return (
                [node.data["last_name"]]
                + collect_names(node.left)
                + collect_names(node.right)
            )

        original_names = sorted(collect_names(self.root))
        max_heap_root = transformer.bstToMaxHeap(self.root)
        heap_names = sorted(collect_names(max_heap_root))
        assert original_names == heap_names

    def test_heapify_empty_tree(self):
        transformer = BSTToHeapTransformer()
        assert transformer.bstToMinHeap(None) is None
        assert transformer.bstToMaxHeap(None) is None
