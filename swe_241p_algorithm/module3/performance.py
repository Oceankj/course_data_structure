import random
import timeit

from group_anagram import GroupAnagram


def generate_data(
    size: int,
    mode: str = "random",
):
    chars = "abcdefghijklmnopqrstuvwxyz"
    if mode == "random":
        return "".join(random.choice(chars) for _ in range(size))
    elif mode == "sorted":
        sorted_chars = sorted([chars[i % len(chars)] for i in range(size)])
        return "".join(sorted_chars)
    elif mode == "reversed":
        reversed_chars = sorted(
            [chars[i % len(chars)] for i in range(size)], reverse=True
        )
        return "".join(reversed_chars)
    elif mode == "few_unique":
        few = "abcde"
        return "".join(random.choice(few) for _ in range(size))
    else:
        raise ValueError("Invalid mode")


def measure_time(sort_func, data, repeat=3):
    total = 0
    for _ in range(repeat):
        input_str = str(data)
        start = timeit.default_timer()
        sort_func(input_str)
        total += timeit.default_timer() - start
    return total / repeat


def compare_sorts(sizes, modes):
    ga = GroupAnagram()
    for size in sizes:
        for mode in modes:
            data = generate_data(size, mode)

            t_merge_sort = measure_time(ga.merge_sort, data, 100)
            t_quick_sorted = measure_time(ga.quick_sort, data, 100)

            print(f"Size={size}, Mode={mode}")
            print(f"merge_sort()={t_merge_sort:.6f}s")
            print(f"quick_sorted ()={t_quick_sorted:.6f}s")
            print("----------------------------------")


compare_sorts([1000], ["random", "sorted", "reversed", "few_unique"])
compare_sorts([100, 1000, 10000], ["random"])
