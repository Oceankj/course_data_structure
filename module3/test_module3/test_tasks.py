import pytest
import os

from module3.read_and_parse import read_and_parse
from module3.hash_data_structure import HashDataStructure


class TestTask1:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.hash_set = HashDataStructure()

    def test_initial_size(self):
        assert self.hash_set.size() == 0

    def test_insert_one(self):
        self.hash_set.insert("apple")
        assert self.hash_set.size() == 1

    def test_insert_another_unique(self):
        self.hash_set.insert("apple")
        self.hash_set.insert("banana")
        assert self.hash_set.size() == 2

    def test_insert_duplicate(self):
        self.hash_set.insert("apple")
        self.hash_set.insert("apple")
        assert self.hash_set.size() == 1

    def test_trigger_resize(self):
        self.hash_set.insert("apple")
        self.hash_set.insert("banana")
        self.hash_set.insert("cherry")
        self.hash_set.insert("date")
        assert self.hash_set.size() == 4

    def test_linear_probing(self):
        self.hash_set.insert("apple")
        self.hash_set.insert("banana")
        self.hash_set.insert("cherry")
        self.hash_set.insert("date")
        self.hash_set.insert("elderberry")
        self.hash_set.insert("fig")
        self.hash_set.insert("grape")
        assert self.hash_set.size() == 7

    def test_python_identity_vs_equality(self):
        a = "".join(["py", "thon"])
        b = "python"
        assert a == b
        assert a is not b  # two different str objects with same content
        self.hash_set.insert(a)
        self.hash_set.insert(b)
        assert self.hash_set.size() == 1


class TestTask2:
    def setup_method(self, method):
        self.temp_files = []

    def teardown_method(self, method):
        for fpath in getattr(self, "temp_files", []):
            if os.path.exists(fpath):
                os.remove(fpath)

    def __create_temp_file(self, content, filename):
        module3_path = os.path.dirname(os.path.abspath(__file__))
        filepath = os.path.join(module3_path, "..", filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        self.temp_files.append(filepath)

    def test_read_and_parse_case_sensitivity(self, capsys):
        sample_txt = "Dog dog DOG dOg DoG\n" "House house HOuSe\n"
        filename = "test_sample_case.txt"
        self.__create_temp_file(sample_txt, filename)

        read_and_parse(filename)
        captured = capsys.readouterr().out
        num = int(captured.strip())
        assert num is not None
        assert num == 8

    def test_read_and_parse_numbers(self, capsys):
        sample_txt = "123 321 213 \n" "456 654 546 123\n"
        filename = "test_sample_numbers.txt"
        self.__create_temp_file(sample_txt, filename)

        read_and_parse(filename)
        captured = capsys.readouterr().out
        num = int(captured.strip())
        assert num is not None
        assert num == 2

    def test_read_and_parse_sample_file(self, capsys):
        sample_txt = (
            "Listen, silent! Enlist.\n"
            "Triangle integral relate alert.\n"
            "A man, a plan, a canal, Panama!\n"
            "Dog God god."
        )
        filename = "test_sample_anagrams.txt"
        self.__create_temp_file(sample_txt, filename)

        read_and_parse(filename)
        captured = capsys.readouterr().out
        num = int(captured.strip())
        assert num is not None
        assert num == 16

    def test_read_and_parse_pride_and_prejudice_runs(self, capsys):
        try:
            read_and_parse("pride-and-prejudice.txt")
            captured = capsys.readouterr().out
            num = int(captured.strip())
            assert num == 6954
        except FileNotFoundError:
            pytest.skip(
                "pride-and-prejudice.txt does not exist in test environment"
            )
