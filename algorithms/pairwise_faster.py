import time
import random


def max_pair_prod(numbers):
    if len(numbers) < 2:
        return ""

    # Initialize variables to store the two greatest numbers
    first_max = second_max = float('-inf')

    # Iterate through the sequence
    for num in numbers:
        if num > first_max:
            second_max = first_max
            first_max = num
        elif num > second_max:
            second_max = num

    # Calculate the product of the two greatest numbers
    product = first_max * second_max

    return product


# Input number of elements
n = int(input())

# Input array
array = list(map(int, input().split()))

# Ensure that the array has at least two elements
if len(array) < 2:
    print("")
else:
    # Example usage:
    result = max_pair_prod(array)
    print(result)

