import os
import pytest
from swe_240p_data_structure.module4.BST import BST

TEST_FILE_PATH = os.path.dirname(__file__)


class TestTask1:
    @pytest.fixture(autouse=True)
    def setUp(self):
        self.bst = BST()

    def test_insert_and_search(self):
        result = self.bst.search("mckay")
        assert result is not None
        print(result.data["raw_data"])
        assert (
            result.data["raw_data"]
            == "8534534McKay                    0251CT  1"
        )

        result = self.bst.search("laporte")
        assert result is not None
        assert result.data["last_name"] == "laporte"

        result = self.bst.search("johnston")
        assert result is not None
        assert result.data["last_name"] == "johnston"

    def test_search_not_found(self):
        result = self.bst.search("unknown")
        assert result is None

    def test_delete_leaf(self):
        self.bst.delete("D8400912Green                    0045RFM 1")
        result = self.bst.search("green")
        assert result is None

        res2 = self.bst.search("laporte")
        assert res2 is not None
        assert res2.data["last_name"] == "laporte"

    def test_delete_root(self):
        self.bst.delete("D8534534McKay                    0251CT  1")
        result = self.bst.search("mckay")
        assert result is None

        assert self.bst.search("laporte") is not None
        assert self.bst.search("black") is not None

    def test_case_insensitive_search(self):
        """Searches should be case-insensitive based on requirements"""
        result = self.bst.search("McKay".lower())
        assert result is not None
        result2 = self.bst.search("MCkay")
        assert result2 is None

    def test_duplicate_insert(self):
        input_duplicate = "I8534534McKay                    0251CT  1"
        self.bst.insert(input_duplicate)
        result = self.bst.search("mckay")
        assert result is not None
        assert (
            result.data["raw_data"]
            == "8534534McKay                    0251CT  1"
        )


class TestTask2:
    def setup_method(self):
        self.tree_file = TEST_FILE_PATH + "/tree_input.txt"
        self.bst = BST()

    def teardown_method(self):
        for fname in [
            "inOrderTraversal.txt",
            "preOrderTraversal.txt",
            "postOrderTraversal.txt",
        ]:
            if os.path.exists(fname):
                os.remove(fname)

    # It might be different if we implemented balance tree
    def test_in_order_traversal_output(self):
        self.bst.inOrderTraversal()
        with open(TEST_FILE_PATH + "/inOrderTraversal.txt", "r") as f:
            expected_lines = [line.rstrip("\n") for line in f]
        with open("inOrderTraversal.txt", "r") as f:
            lines = [line.rstrip("\n") for line in f]
        assert lines == expected_lines

    # It might be different if we implemented balance tree
    def test_pre_order_traversal_output(self):
        self.bst.preOrderTraversal()
        with open(TEST_FILE_PATH + "/preOrderTraversal.txt", "r") as f:
            expected_lines = [line.rstrip("\n") for line in f]
        with open("preOrderTraversal.txt", "r") as f:
            lines = [line.rstrip("\n") for line in f]
        assert lines == expected_lines

    # It might be different if we implemented balance tree
    def test_post_order_traversal_output(self):
        self.bst.postOrderTraversal()
        with open(TEST_FILE_PATH + "/postOrderTraversal.txt", "r") as f:
            expected_lines = [line.rstrip("\n") for line in f]
        with open("postOrderTraversal.txt", "r") as f:
            lines = [line.rstrip("\n") for line in f]
        assert lines == expected_lines


class TestTask3:
    def setup_method(self):
        self.tree_file = TEST_FILE_PATH + "/tree_input.txt"
        self.bst = BST()

    def teardown_method(self):
        for fname in [
            "levelOrderTraversal.txt",
        ]:
            if os.path.exists(fname):
                os.remove(fname)

    # It might be different if we implemented balance tree
    def test_level_order_traversal_output(self):
        self.bst.levelOrderTraversal()
        with open(TEST_FILE_PATH + "/levelOrderTraversal.txt", "r") as f:
            expected_lines = [line.rstrip("\n") for line in f]
        with open("levelOrderTraversal.txt", "r") as f:
            lines = [line.rstrip("\n") for line in f]
        assert lines == expected_lines
