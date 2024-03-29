import random

array_to_sort = [50, 19, 27, 33, 42, 16, 7, 11, 49, 3,
                 25, 8, 36, 14, 21, 29, 45, 5, 38, 1,
                 30, 20, 46, 4, 13, 26, 10, 47, 17, 6,
                 35, 9, 24, 48, 15, 2, 28, 44, 23, 37,
                 12, 43, 18, 40, 22, 31, 39, 34, 41, 32]
# for nums in array_to_sort:
print(f"Unsorted array {array_to_sort}")

# Bubble sort implementation
for i in range(len(array_to_sort)):
    for j in range(len(array_to_sort) - 1):  # Corrected range
        if array_to_sort[j] > array_to_sort[j + 1]:  # Compare adjacent elements
            # Swap the elements if they are in the wrong order
            array_to_sort[j], array_to_sort[j + 1] = array_to_sort[j + 1], array_to_sort[j]

print(f"Sorted array {array_to_sort}")

array_to_sorts = [random.sample(range(100), 100)]
