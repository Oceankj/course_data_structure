Task Description: Complete the following task.

Task-1: Implement a Hash data structure from scratch, without using any built-in Hash or Dictionary APIs. You may utilize a built-in Array or List, or your custom-built LinkedList as the underlying storage. Your Hash class should expose the following:

- **Fields:**
    - `HashTable`: a fixed-size array or list (can be 1D or 2D, depending on your hash function)

- **Methods:**
    - `hash(x)`: takes a string `x` and returns an integer index for the hashtable (implement your choice of hash function with a collision resolution strategy)
    - `insert(x)`: inserts string `x` into the hashtable at the location determined by `hash(x)`
    - `size()`: returns the count of unique keys in the hashtable

Write sample test cases to validate your implementation.

Task-2: Use your implemented hashtable to determine the number of unique anagram-root words in the file `pride-and-prejudice.txt`. Follow these steps:

1. **Read and Parse:** Read the file line by line to avoid loading the whole file into memory. For each line, split it into words using non-alphanumeric characters (e.g., `\n`, `\t`, `,`, `.`, etc.) as delimiters.
2. **Anagram-root Definition:** An anagram is a word created by rearranging the letters of another word, using all original letters. The *anagram-root* of a word is obtained by sorting its characters (e.g., the root for both `mango` and `gonma` is `agmno`).
3. **Process:** For each parsed word:
   - Sort the word's characters to find its anagram-root (you may use any built-in sorting API).
   - Insert the anagram-root into your hashtable. If it already exists, skip it.
4. **Count:** After processing the entire file, use `size()` on your Hash class to find the number of unique anagram-root words.

Be sure to validate your implementation with sample test cases.