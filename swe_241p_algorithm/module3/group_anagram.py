class GroupAnagram:
    def solution(self, input: list[str]) -> list[list[str]]:
        dictionary: dict[str, list[str]] = {}
        for string in input:
            sorted_string = self.sort_string(string)
            dictionary.setdefault(sorted_string, []).append(string)
        return list(dictionary.values())

    def sort_string(self, string: str) -> str:
        return self.merge_sort(string)
        # return self.quick_sort(string)

    def merge_sort(self, string: str) -> str:
        if len(string) <= 1:
            return string

        mid = len(string) // 2
        left = self.merge_sort(string[:mid])
        right = self.merge_sort(string[mid:])

        return self.__merge(left, right)

    def __merge(self, left, right) -> str:
        result = ""
        left_i = right_i = 0
        while left_i < len(left) and right_i < len(right):
            left_c = left[left_i]
            right_c = right[right_i]
            if left_c <= right_c:
                result += left_c
                left_i += 1
            else:
                result += right_c
                right_i += 1

        # Add remaining elements
        result += left[left_i:]
        result += right[right_i:]

        return result

    def quick_sort(self, string: str) -> str:
        str_array: list[str] = list(string)
        self.__sort(str_array, 0, len(str_array) - 1)
        return "".join(str_array)

    def __sort(self, str_array: list[str], left: int, right: int):
        if left >= right:
            return
        pivotIndex = self.__sorted_by_pivot(str_array, left, right)
        self.__sort(str_array, left, pivotIndex - 1)
        self.__sort(str_array, pivotIndex + 1, right)

    def __sorted_by_pivot(
        self, str_array: list[str], left: int, right: int
    ) -> int:
        pivot = str_array[right]
        i = left - 1
        for j in range(left, right):
            if str_array[j] < pivot:
                i = i + 1
                str_array[i], str_array[j] = str_array[j], str_array[i]
        str_array[i + 1], str_array[right] = str_array[right], str_array[i + 1]
        return i + 1
