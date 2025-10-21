import pytest
from swe_241p_algorithm.module2.task1 import Solution


class TestTask1:
    @pytest.fixture(autouse=True)
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        nums = [4, 9, 10, 13, 17, 17, 19, 21]
        target = 17
        expected = [4, 5]
        result = self.sol.solution(nums, target)
        assert result == expected

    def test_example2(self):
        nums = [2, 4, 6, 8, 10, 14, 16]
        target = 12
        expected = [-1, -1]
        result = self.sol.solution(nums, target)
        assert result == expected

    def test_example3(self):
        nums = []
        target = 0
        expected = [-1, -1]
        result = self.sol.solution(nums, target)
        assert result == expected

    # Additional sample test cases
    def test_target_at_beginning(self):
        nums = [1, 1, 2, 3, 4]
        target = 1
        expected = [0, 1]
        result = self.sol.solution(nums, target)
        assert result == expected

    def test_target_at_end(self):
        nums = [2, 3, 4, 4, 4]
        target = 4
        expected = [2, 4]
        result = self.sol.solution(nums, target)
        assert result == expected

    def test_target_not_found(self):
        nums = [1, 2, 3, 4, 5]
        target = 6
        expected = [-1, -1]
        result = self.sol.solution(nums, target)
        assert result == expected

    def test_single_element_found(self):
        nums = [5]
        target = 5
        expected = [0, 0]
        result = self.sol.solution(nums, target)
        assert result == expected

    def test_single_element_not_found(self):
        nums = [5]
        target = 3
        expected = [-1, -1]
        result = self.sol.solution(nums, target)
        assert result == expected
