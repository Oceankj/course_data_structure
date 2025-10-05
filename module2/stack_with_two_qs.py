from typing import Any
from module2.queue import Queue


class StackWithTwoQs:
    def __init__(self) -> None:
        self.queueOne = Queue()
        self.queueTwo = Queue()

    def push(self, value: Any) -> None:
        while self.queueOne.size() > 0:
            self.queueTwo.enqueue(self.queueOne.dequeue())

        self.queueOne.enqueue(value)

        while self.queueTwo.size() > 0:
            self.queueOne.enqueue(self.queueTwo.dequeue())

    def pop(self) -> Any:
        return self.queueOne.dequeue()

    def peek(self) -> Any:
        return self.queueOne.poll()

    def size(self) -> int:
        return self.queueOne.size()
