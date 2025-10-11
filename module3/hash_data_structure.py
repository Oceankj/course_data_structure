from typing import List, Optional


class HashDataStructure:
    def __init__(self) -> None:
        self.__len = 0
        self.__list: List[Optional[str]] = [None] * 7

    def hash(self, key: str, list_leng: int) -> int:
        hash_code = self.__hash_function(key)
        index = self.__compression_function(hash_code, list_leng)
        # linear probing
        while self.__list[index] is not None and self.__list[index] != key:
            hash_code += 1
            index = self.__compression_function(hash_code, list_leng)
        return index

    def __hash_function(self, key: str) -> int:
        mask = (1 << 32) - 1
        h = 0
        for character in key:
            # Shift h left by n bits (with wrap-around via cyclic shift)
            h = ((h << 5) & mask) | (h >> (32 - 5))
            h += ord(character)
        return h

    def __compression_function(self, hash_code: int, list_leng: int) -> int:
        return hash_code % list_leng

    def __resize(self):
        next_prime = self.__next_prime(len(self.__list))
        prev_list = self.__list
        self.__list = [None] * next_prime

        for key in prev_list:
            if key is None:
                continue
            index = self.hash(key, next_prime)
            self.__list[index] = key

    def __next_prime(self, num: int) -> int:
        def is_prime(x: int):
            if x < 2:
                return False
            for i in range(2, int(x**0.5) + 1):
                if x % i == 0:
                    return False
            return True

        candidate = max(2, num * 2)
        while not is_prime(candidate):
            candidate += 1
        return candidate

    def insert(self, key: str):
        list_length = len(self.__list)
        index = self.hash(key, list_length)
        if self.__list[index] == key:
            return

        self.__list[index] = key
        self.__len += 1
        if self.__len > list_length / 2:
            self.__resize()

    def size(self):
        return self.__len
