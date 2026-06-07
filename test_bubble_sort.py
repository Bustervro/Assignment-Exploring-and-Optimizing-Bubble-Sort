from bubble_sort import bubble_sort_basic, bubble_sort_optimized

test_cases = [
    [5, 2, 9, 1, 6],
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1],
    [7, 7, 7, 7],
    [],
    [10]
]

for test in test_cases:
    print("Original:", test)
    print("Basic Sort:", bubble_sort_basic(test))
    print("Optimized Sort:", bubble_sort_optimized(test))
    print("-" * 30)
