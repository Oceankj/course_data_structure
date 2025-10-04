import pytest
from ..stack import Stack


class TestTask1:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.stack = Stack()

    def test_initial_stack_is_empty(self):
        assert self.stack.size() == 0

    def test_push_increases_size(self):
        self.stack.push(10)
        assert self.stack.size() == 1
        self.stack.push(20)
        assert self.stack.size() == 2

    def test_push_and_peek(self):
        self.stack.push(5)
        self.stack.push(15)

        assert self.stack.peek() == 15
        assert self.stack.size() == 2

    def test_push_and_pop(self):
        self.stack.push("a")
        self.stack.push("b")
        val = self.stack.pop()
        assert val == "b"
        assert self.stack.size() == 1
        val2 = self.stack.pop()
        assert val2 == "a"
        assert self.stack.size() == 0

    def test_pop_empty_raises(self):
        with pytest.raises(ValueError):
            self.stack.pop()

    def test_peek_empty_raises(self):
        with pytest.raises(ValueError):
            self.stack.peek()

    def test_mixed_operations(self):
        self.stack.push(1)
        self.stack.push(2)
        assert self.stack.pop() == 2
        self.stack.push(3)
        assert self.stack.peek() == 3
        assert self.stack.pop() == 3
        assert self.stack.pop() == 1
        assert self.stack.size() == 0

    def test_push_various_types(self):
        self.stack.push(42)
        self.stack.push("hello")
        self.stack.push([1, 2, 3])
        assert self.stack.pop() == [1, 2, 3]
        assert self.stack.pop() == "hello"
        assert self.stack.pop() == 42
