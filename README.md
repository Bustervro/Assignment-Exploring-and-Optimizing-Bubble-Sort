# Assignment-Exploring-and-Optimizing-Bubble-Sort
Bubble Sort Report

This project implements Bubble Sort in Python. I created two versions: a basic Bubble Sort and an optimized Bubble Sort.

The basic Bubble Sort works by comparing two numbers next to each other. If the left number is bigger than the right number, the algorithm swaps them. This repeats until the whole list is sorted.

The optimized Bubble Sort uses a swapped variable. If the list goes through one full pass without swapping anything, that means the list is already sorted, so the algorithm stops early.

Test Cases:

1. Random array:
Input: [5, 2, 9, 1, 6]
Output: [1, 2, 5, 6, 9]

2. Already sorted array:
Input: [1, 2, 3, 4, 5]
Output: [1, 2, 3, 4, 5]

3. Descending array:
Input: [5, 4, 3, 2, 1]
Output: [1, 2, 3, 4, 5]

4. Identical elements:
Input: [7, 7, 7, 7]
Output: [7, 7, 7, 7]

5. Empty array:
Input: []
Output: []

6. Single element:
Input: [10]
Output: [10]

Time Complexity:

Bubble Sort has O(n^2) time complexity in the average and worst case because it uses nested loops. Each number may need to be compared with many other numbers.

The best case for the optimized version is O(n), because if the list is already sorted, it stops after one pass.

Space Complexity:

Bubble Sort uses O(1) extra space because it sorts by swapping elements inside the list. This makes it an in-place sorting algorithm.

Stability:

Bubble Sort is stable because it does not change the order of equal elements. Equal numbers stay in the same relative order.

Optimization Observation:

The optimized version is faster when the list is already sorted. The basic version still checks many times, but the optimized version stops early when no swaps happen.
