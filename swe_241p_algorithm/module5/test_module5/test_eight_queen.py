from swe_241p_algorithm.module5.eight_queen import eight_queen


class TestEightQueen:

    def test_example_1(self):
        board = [1, 2, 3, 4, 5, 6, 7, 8]
        assert eight_queen(board) == 7

    def test_example_2(self):
        board = [1, 1, 1, 1, 1, 1, 1, 1]
        assert eight_queen(board) == 7

    def test_all_queens_already_valid(self):
        # A valid solution
        board = [1, 5, 8, 6, 3, 7, 2, 4]
        assert eight_queen(board) == 0

    def test_one_queen_needs_to_move(self):
        # One queen overlaps, so move needed
        board = [1, 5, 8, 6, 3, 7, 2, 2]  # Last queen conflicts in col
        assert eight_queen(board) == 1

    def test_reverse_board(self):
        # Reverse of example solution
        board = [4, 2, 7, 3, 6, 8, 5, 1]
        assert eight_queen(board) == 0

    def test_random_invalid(self):
        board = [2, 4, 6, 8, 1, 3, 5, 8]
        # The last 8 repeats, so at least 1 move; more may be required for validity
        assert eight_queen(board) > 0

    def test_zero_board(self):
        # Zeros should be interpreted as empty and require placement
        board = [0] * 8
        # Minimum moves needed is 8 (since every queen needs to be placed)
        assert eight_queen(board) == 8

    def test_partial_queens(self):
        # Mix of zeros and existing queens
        board = [1, 0, 0, 6, 0, 7, 0, 4]
        assert 0 <= eight_queen(board) <= 5
