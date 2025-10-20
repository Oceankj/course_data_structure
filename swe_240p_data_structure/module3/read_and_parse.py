import os
import re

from .hash_data_structure import HashDataStructure

module3_path = os.path.dirname(os.path.abspath(__file__))


def read_and_parse(file_name: str = "pride-and-prejudice.txt"):
    file_path = os.path.join(module3_path, file_name)
    f = open(file_path, "r", encoding="utf-8")
    hash_set = HashDataStructure()

    # count = 0
    # for line in f:
    #     count += 1
    # indicator = Indicator(count)

    f.seek(0)
    for line in f:
        words = re.split(r"[^0-9a-zA-Z]+", line)
        for w in words:
            if not w:
                continue
            anagram = "".join(sorted(w))
            hash_set.insert(anagram)
        # indicator.add()

    f.close()
    print(hash_set.size())


# class Indicator:
#     def __init__(self, taskTotal: int) -> None:
#         self.total = taskTotal
#         self.count = 0

#     def add(self, amount=1):
#         self.count += amount
#         if self.count % 100 == 0:
#             print(f"{self.count / self.total * 100:.2f}%")
