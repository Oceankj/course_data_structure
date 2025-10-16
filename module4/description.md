Task Description:

You are given an input ASCII text file containing an arbitrary number of student records in the following format:

```
    Operation code: 1 character ('I' for insert, 'D' for delete)
    Student number: 7 characters
    Student last name: 25 characters
    Home department: 4 characters
    Program: 4 characters
    Year: 1 character
```
Each record is stored as one line in the text file; i.e., there is a newline character immediately following the year.


- Task-1: Build a Binary Search Tree (BST) using the data from the input file Download input file. Both insertion into and deletion from the tree will be done. The tree should be ordered by the student's last name (use a case-insensitive comparison). There are only unique records in the input file. Each node must contain the student data (exclude the operation code), a left child pointer, and a right child pointer. A parent pointer is optional but might prove helpful in some operations.

- Task-2: Traverse the binary search tree recursively, printing out the nodes in ascending logical order; i.e., do a depth-first, in-order tree traversal. Print the node data to a text file.

- Task-3: Traverse the binary search tree, starting at the top level (the root node), and proceeding downwards level-by-level. At each level, print out the nodes from left to right. In other words, do a breadth-first traversal. You may have to use a queue to implement this. Print the node data to a text file.