# Task Description

A heap is a binary tree where each node can have at most two children – the left child and the right child. For a min-heap, the value of each node must be less than or equal to the values of its children (i.e., the minimum value is at the root). For a max-heap, the value of each node must be greater than or equal to the values of its children (i.e., the maximum value is at the root). Due to the heap order property, the root of the heap is always the minimum (in a min-heap) or maximum (in a max-heap) element, making it easy to access the most significant element without having to search through the entire data structure.

**Task-1:** Given a list of integers, write a class HeapBuilder that takes the integer list, creates a heap, and returns that heap as a binary tree. You have to implement both Max-Heap and Min-Heap. Write sample test cases to validate your implementation.

```java
class Node {
    int data;
    Node left;
    Node right;

    Node(int data) {
        this.data = data;
        this.left = null;
        this.right = null;
    }
}

class HeapBuilder {
    // Builds and returns the root node of a min-heap binary tree
    Node createMinHeap(List<Integer> values);

    // Builds and returns the root node of a max-heap binary tree
    Node createMaxHeap(List<Integer> values);
}

```


**Task-2:** Write a class BSTToHeapTransformer that takes the root node of a BST and converts it into a Min-Heap and Max-Heap. To write this BSTToHeapTransformer class, You must utilize your implemented BST class. Write sample test cases to validate your implementation.

```java
class BSTToHeapTransformer {
    // Returns a binary tree as a min-heap based on the input BST
    List<Node> bstToMinHeap(BST bst);

    // Returns a binary tree as a max-heap based on the input BST
    List<Node> bstToMaxHeap(BST bst);
}
```