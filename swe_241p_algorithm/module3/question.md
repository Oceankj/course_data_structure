# Task Description

An **Anagram** is a word or phrase formed by rearranging the letters of another word or phrase, typically using all the original letters exactly once.  
For example, **"mango"** and **"ogman"** are anagrams.

## Task 1: Group Anagrams

Given an array of strings `strings`, group the words that are anagrams of each other.  
You can return the answer in any order.

**Example**

- **Input:**  
  `strings = ["bucket", "rat", "mango", "tango", "ogtan", "tar"]`

- **Output:**  
  `[["bucket"], ["rat", "tar"], ["mango"], ["tango", "ogtan"]]`

---

## Assignment Steps

**Step 1:**  
Implement a function  
`List<List<String>> groupAnagram(List<String> strings)`  
that takes a list of strings and returns a list of lists of strings, where each sublist contains words that are anagrams of each other.

**Step 2:**  
To group the anagrams, you will need to sort the characters of each string (according to their ASCII codes). Strings that, when sorted, result in the same sequence of characters should be grouped together (i.e., in the same "anagram bucket").  
For example, after sorting, both `"mango"` and `"ogman"` become `"agmno"` and so they are grouped together.

Implement a function  
`String sortString(String str)`  
that sorts the characters in a string.

> **Do not use built-in sorting functions.**  
> Instead, implement two of the following sorting algorithms on your own, and compare their performance.  
> Write sample test cases to validate your implementation.

- Mergesort
- Quicksort
- Heapsort
- Radix sort