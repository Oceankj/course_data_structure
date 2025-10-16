from collections import deque
import os
from typing import Callable, Deque, Optional, TypedDict

TREE_INPUT_PATH = os.path.join(os.path.dirname(__file__), "tree_input.txt")


class StudentRecord(TypedDict):
    last_name: str
    raw_data: str


class Node:
    def __init__(self, input: str = ""):
        if len(input) > 0:
            self.data: StudentRecord = self.__parse_data(input)
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

    def __parse_data(self, input: str) -> StudentRecord:
        return {
            "last_name": input[8:33].strip().lower(),
            "raw_data": input[1:],
        }


class BST:
    def __init__(self):
        self.root = None
        self.__read_file()

    def __read_file(self):
        with open(TREE_INPUT_PATH, encoding="utf-8") as f:
            inputs = [line.rstrip("\n") for line in f if line.strip() != ""]
            for line in inputs:
                if line[0] == "I":
                    self.insert(line)
                elif line[0] == "D":
                    self.delete()

    def insert(self, input: str):
        node = Node(input)
        self.root = self.__add_node(node, self.root)
        # balance
        pass

    def __add_node(self, node: Node, parent: Optional[Node] = None) -> Node:
        if parent is None:
            return node
        if node.data["last_name"] > parent.data["last_name"]:
            parent.right = self.__add_node(node, parent.right)
        else:
            parent.left = self.__add_node(node, parent.left)
        return parent

    def search(self, name: str) -> Node | None:
        return self.__search_subtree(name, self.root)

    def __search_subtree(self, name: str, node: Optional[Node]) -> Node | None:
        if node is None:
            return None
        if node.data["last_name"] == name:
            return node
        elif node.data["last_name"] > name:
            return self.__search_subtree(name, node.left)
        else:
            return self.__search_subtree(name, node.right)

    def delete(self, input: str):
        last_name = input[8:33].strip().lower()
        self.root = self.__delete_subtree(last_name, self.root)

    def __delete_subtree(self, name: str, node: Optional[Node]):
        if node is None:
            return None
        if node.data["last_name"] < name:
            node.right = self.__delete_subtree(name, node.right)
        elif node.data["last_name"] > name:
            node.left = self.__delete_subtree(name, node.left)
        else:
            if node.left is None and node.right is None:
                return None
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            minNode = self.__find_min(node.right)
            node.data = minNode.data
            node.right = self.__delete_subtree(
                minNode.data["last_name"], node.right
            )
        return node

    def __find_min(self, node: Node):
        if node.left is None:
            return node
        return self.__find_min(node.left)

    # depth-first traversal
    def __traversal_generator(
        self,
        node: Node | None,
        previsit: Optional[Callable[["Node"], None]] = None,
        invisit: Optional[Callable[["Node"], None]] = None,
        postvisit: Optional[Callable[["Node"], None]] = None,
    ):
        if node is None:
            return
        if previsit is not None:
            yield previsit(node)

        yield from self.__traversal_generator(
            node.left, previsit, invisit, postvisit
        )

        if invisit is not None:
            yield invisit(node)

        yield from self.__traversal_generator(
            node.right, previsit, invisit, postvisit
        )

        if postvisit is not None:
            yield postvisit(node)

    def inOrderTraversal(self):
        with open("inOrderTraversal.txt", "w") as file:
            for input in self.__traversal_generator(
                self.root, invisit=lambda node: node.data["raw_data"]
            ):
                file.write(input + "\n")

    def preOrderTraversal(self):
        with open("preOrderTraversal.txt", "w") as file:
            for input in self.__traversal_generator(
                self.root, previsit=lambda node: node.data["raw_data"]
            ):
                file.write(input + "\n")

    def postOrderTraversal(self):
        with open("postOrderTraversal.txt", "w") as file:
            for input in self.__traversal_generator(
                self.root, postvisit=lambda node: node.data["raw_data"]
            ):
                file.write(input + "\n")

    # breadth-first traversal
    def levelOrderTraversal(self) -> None:
        with open("levelOrderTraversal.txt", "w") as file:
            queue: Deque[Optional[Node]] = deque()
            queue.append(self.root)

            while len(queue) != 0:
                node = queue.pop()
                if node is None:
                    continue
                queue.append(node.left)
                queue.append(node.right)
                file.write(node.data["raw_data"] + "\n")
 