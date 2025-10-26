import pytest
from swe_241p_algorithm.module3.group_anagram import GroupAnagram


class TestGroupAnagram:
    @pytest.fixture(autouse=True)
    def setUp(self):
        self.sol = GroupAnagram()

    def test_example_from_question_md(self):
        strs = ["bucket", "rat", "mango", "tango", "ogtan", "tar"]
        expected = [["bucket"], ["rat", "tar"], ["mango"], ["tango", "ogtan"]]
        result = self.sol.solution(strs)
        # Convert inner lists to sets for comparison regardless of order
        assert sorted([set(g) for g in result]) == sorted(
            [set(g) for g in expected]
        )

    def test_single_word(self):
        strs = ["hello"]
        expected = [["hello"]]
        result = self.sol.solution(strs)
        assert result == expected

    def test_empty_input(self):
        strs = []
        expected = []
        result = self.sol.solution(strs)
        assert result == expected

    def test_no_anagrams(self):
        strs = ["abc", "def", "ghi"]
        expected = [["abc"], ["def"], ["ghi"]]
        result = self.sol.solution(strs)
        assert sorted([set(g) for g in result]) == sorted(
            [set(g) for g in expected]
        )

    def test_all_anagrams(self):
        strs = ["abcd", "bcda", "cdab", "dabc"]
        expected = [["abcd", "bcda", "cdab", "dabc"]]
        result = self.sol.solution(strs)
        assert sorted([set(g) for g in result]) == sorted(
            [set(g) for g in expected]
        )

    # Part2
    def test_merge_sort_simple(self):
        assert self.sol.merge_sort("cba") == "abc"
        assert self.sol.merge_sort("a") == "a"
        assert self.sol.merge_sort("") == ""
        assert self.sol.merge_sort("edcba") == "abcde"

    def test_merge_sort_with_duplicates(self):
        assert self.sol.merge_sort("banana") == "aaabnn"
        assert self.sol.merge_sort("mississippi") == "iiiimppssss"

    def test_merge_sort_already_sorted(self):
        assert self.sol.merge_sort("abcdefg") == "abcdefg"

    def test_quick_sort_simple(self):
        assert self.sol.quick_sort("cba") == "abc"
        assert self.sol.quick_sort("a") == "a"
        assert self.sol.quick_sort("") == ""
        assert self.sol.quick_sort("edcba") == "abcde"

    def test_quick_sort_with_duplicates(self):
        assert self.sol.quick_sort("banana") == "aaabnn"
        assert self.sol.quick_sort("mississippi") == "iiiimppssss"

    def test_quick_sort_already_sorted(self):
        assert self.sol.quick_sort("abcdefg") == "abcdefg"
