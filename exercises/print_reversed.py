# Given an array, A, of N integers, print A's elements in reverse order as a single line of space-separated numbers.

n = int(input("What is the array length: \n"))

arr = []

for i in range(1, n+1):
    arr.append(i)

# Reverse the array using slicing notation
reversed_arr = arr[::-1]

# Print the reversed array in the specified format
print(' '.join(map(str, reversed_arr)))
