# Task1
class FindFirstAndLastPosition:

    def solution(self, input: list[int], target: int) -> list[int]:
        if len(input) == 0:
            return [-1, -1]

        start_index = self.__find_start_index(input, target)
        if start_index == -1:
            return [-1, -1]

        end_index = self.__find_end_index(input, target)
        return [start_index, end_index]

    def __find_start_index(self, input: list[int], target: int) -> int:
        left = 0
        right = len(input) - 1

        while left < right:
            mid = (left + right) // 2
            mid_value = input[mid]
            if target < mid_value:
                right = mid - 1
            elif mid_value < target:
                left = mid + 1
            else:
                right = mid

        return left if input[left] == target else -1

    def __find_end_index(self, input: list[int], target: int) -> int:
        left = 0
        right = len(input) - 1

        while left < right:
            # Slightly move to right to aviod infinity loop
            mid = (left + right + 1) // 2
            mid_value = input[mid]

            if target < mid_value:
                right = mid - 1
            elif mid_value < target:
                left = mid + 1
            else:
                left = mid

        return left if input[left] == target else -1
