def bubble_sort_basic(arr):
    # Make a copy so the original list does not change
    numbers = arr.copy()
    n = len(numbers)

    # Go through the list many times
    for i in range(n):
        # Compare numbers next to each other
        for j in range(0, n - i - 1):
            # Swap if the left number is bigger than the right number
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    return numbers


def bubble_sort_optimized(arr):
    # Make a copy so the original list does not change
    numbers = arr.copy()
    n = len(numbers)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                swapped = True

        # If no swaps happened, the list is already sorted
        if swapped == False:
            break

    return numbers
