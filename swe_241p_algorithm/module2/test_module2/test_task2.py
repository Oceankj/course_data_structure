import pytest
from swe_241p_algorithm.module2.task2 import Solution


class TestTask2:
    @pytest.fixture(autouse=True)
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        target = 3
        expected = True
        result = self.sol.solution(matrix, target)
        assert result == expected

    def test_example2(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        target = 13
        expected = False
        result = self.sol.solution(matrix, target)
        assert result == expected

    def test_single_element_found(self):
        matrix = [[42]]
        target = 42
        expected = True
        result = self.sol.solution(matrix, target)
        assert result == expected

    def test_single_element_not_found(self):
        matrix = [[100]]
        target = 17
        expected = False
        result = self.sol.solution(matrix, target)
        assert result == expected

    def test_last_element(self):
        matrix = [[1, 2], [3, 4]]
        target = 4
        expected = True
        result = self.sol.solution(matrix, target)
        assert result == expected
