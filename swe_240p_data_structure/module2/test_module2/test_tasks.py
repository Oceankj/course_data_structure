from math import nan
import pytest

from ..queue import Queue
from ..calculator import calculator
from ..stack import Stack
from ..stack_with_two_qs import StackWithTwoQs


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


class TestTask2:
    def test_calculator_simple_expression(self):
        assert calculator("10 + 20 * 2") == 50

    def test_calculator_invalid_operand(self):
        assert calculator("foo / 30 + 7") is nan

    def test_calculator_division_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            calculator("10 / 0")

    def test_calculator_with_spaces(self):
        assert calculator("  100   +  200 * 3 ") == 700

    def test_calculator_negative_number(self):
        with pytest.raises(ValueError):
            calculator("-10 + 5")

    def test_calculator_single_number(self):
        assert calculator("42") == 42

    def test_calculator_invalid_operator(self):
        assert calculator("10 $ 2") is nan

    def test_calculator_multiple_operations(self):
        assert calculator("2 + 3 * 4 - 5") == 9

    def test_calculator_subtract_and_add(self):
        assert calculator("2 - 3 + 4") == 3

    def test_calculator_only_spaces(self):
        assert calculator("    ") is nan

    def test_calculator_empty_string(self):
        assert calculator("") is nan

    def test_calculator_float_number(self):
        assert calculator("3.5 + 2") is nan

    def test_calculator_double_operator(self):
        with pytest.raises(ValueError):
            calculator("10 ++ 2")

    def test_calculator_large_numbers(self):
        assert calculator("12345 + 67890") == 80235

    def test_calculator_multiple_multiplications(self):
        assert calculator("2 * 3 * 4") == 24

    def test_calculator_multiple_divisions(self):
        assert calculator("100 / 5 / 2") == 10

    def test_calculator_non_integer_division(self):
        assert calculator("7 / 2") == 3.5

    def test_calculator_mixed_operations(self):
        assert calculator("2 + 3 * 4 / 2 - 1") == 7

    def test_calculator_leading_zero(self):
        assert calculator("0 + 5 * 2") == 10

    def test_calculator_long_expression(self):
        expr = "1 + 2 - 3 + 4 - 5 + 6 * 2 / 3"
        assert calculator(expr) == 3

    def test_operactor_in_the_start(self):
        with pytest.raises(ValueError):
            calculator("* 1 + 2 - 3 + 4 - 5 + 6 * 2 / 3")

    def test_operactor_in_the_end(self):
        with pytest.raises(ValueError):
            calculator("1 + 2 - 3 + 4 - 5 + 6 * 2 / 3 %")


class TestTask3:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.q = Queue()

    def test_enqueue_and_dequeue(self):
        self.q.enqueue(1)
        self.q.enqueue(2)
        self.q.enqueue(3)
        assert self.q.dequeue() == 1
        assert self.q.dequeue() == 2
        assert self.q.dequeue() == 3

    def test_dequeue_empty_raises(self):
        with pytest.raises(ValueError):
            self.q.dequeue()

    def test_poll(self):
        self.q.enqueue(10)
        self.q.enqueue(20)
        assert self.q.poll() == 10
        self.q.dequeue()
        assert self.q.poll() == 20

    def test_poll_empty_raises(self):
        with pytest.raises(ValueError):
            self.q.poll()

    def test_size(self):
        assert self.q.size() == 0
        self.q.enqueue(5)
        assert self.q.size() == 1
        self.q.enqueue(6)
        assert self.q.size() == 2
        self.q.dequeue()
        assert self.q.size() == 1

    def test_mixed_operations(self):
        self.q.enqueue("a")
        self.q.enqueue("b")
        assert self.q.poll() == "a"
        assert self.q.dequeue() == "a"
        self.q.enqueue("c")
        assert self.q.dequeue() == "b"
        assert self.q.dequeue() == "c"
        assert self.q.size() == 0


class TestTask4:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.stack = StackWithTwoQs()

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
        with pytest.raises(Exception):
            self.stack.pop()

    def test_peek_empty_raises(self):
        with pytest.raises(Exception):
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
