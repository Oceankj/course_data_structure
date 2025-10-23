# Part2

I implemented the sorting function using both merge sort and quick sort.
Both algorithms are based on the concept of *divide and conquer*.
In theory, their time complexity is **O(n log n)**.

The following table shows the average runtime (in seconds) of each algorithm after running 100 tests with input strings of length 1000.

```
Size=1000, Mode=random
merge_sort() = 0.001919s
quick_sort() = 0.001738s
----------------------------------
Size=1000, Mode=sorted
merge_sort() = 0.001255s
quick_sort() = 0.002393s
----------------------------------
Size=1000, Mode=reversed
merge_sort() = 0.001411s
quick_sort() = 0.002898s
----------------------------------
Size=1000, Mode=few_unique
merge_sort() = 0.001821s
quick_sort() = 0.004879s
----------------------------------
```

For random strings, **quick sort** is slightly faster.
However, when the data is already **sorted** or **reversed**, **merge sort** performs about twice as fast as quick sort.
For **few unique** strings, quick sort takes more than twice the time of merge sort.

This suggests that **merge sort** performs better when the data is more structured or regular.

```
Size=100, Mode=random
merge_sort() = 0.000149s
quick_sort() = 0.000072s
----------------------------------
Size=1000, Mode=random
merge_sort() = 0.001951s
quick_sort() = 0.001648s
----------------------------------
Size=10000, Mode=random
merge_sort() = 0.027210s
quick_sort() = 0.095266s
----------------------------------
```

From the results above, we can also observe that **quick sort** performs better on **smaller datasets**,
while **merge sort** becomes more efficient as the data size increases.