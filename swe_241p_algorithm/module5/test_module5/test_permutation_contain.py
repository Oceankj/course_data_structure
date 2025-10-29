from swe_241p_algorithm.module5.permutation_contain import PermutationContains


def test_permutation_contains_case1():
    assert PermutationContains("ab", "eidbaooo") == True


def test_permutation_contains_case2():
    assert PermutationContains("ab", "eidboaoo") == False


def test_permutation_contains_case3():
    assert PermutationContains("a", "a") == True


def test_permutation_contains_case4():
    assert PermutationContains("abc", "ccccbbbbaaaa") == False


def test_permutation_contains_case5():
    assert PermutationContains("adc", "dcda") == True


def test_permutation_contains_case6():
    assert PermutationContains("", "anything") == True


def test_permutation_contains_case7():
    assert PermutationContains("a", "") == False


def test_permutation_contains_case8():
    assert PermutationContains("xyz", "afdgzyxksldfm") == True


def test_permutation_contains_case9():
    assert PermutationContains("abcdef", "ghijkl") == False
