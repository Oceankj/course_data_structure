def PermutationContains(s1: str, s2: str) -> bool:
    if len(s1) == 0:
        return True
    if len(s2) == 0:
        return False
    character_list: list[int] = [0] * 26

    for i in range(0, len(s1)):
        character_list[ord(s1[i]) - ord("a")] += 1

    for j in range(0, len(s2)):
        if dfs(s2, j, character_list, len(s1)):
            return True

    return False


def dfs(
    input: str, index: int, character_list: list[int], remain_c: int
) -> bool:
    if index == len(input):
        return False

    cIndex = ord(input[index]) - ord("a")
    if character_list[cIndex] > 0:
        remain_c -= 1
        character_list[cIndex] -= 1
        is_permutation = False
        if remain_c == 0:
            is_permutation = True
        else:
            is_permutation = dfs(input, index + 1, character_list, remain_c)

        remain_c += 1
        character_list[cIndex] += 1
        if is_permutation:
            return True
    return False
