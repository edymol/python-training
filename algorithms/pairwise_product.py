import random
import time

# Generate a list of random numbers
numbers = [7, 5, 14, 2, 8, 8, 10, 1, 2, 3]
non_duplicates = set(numbers)
print(non_duplicates)

# Get the number from the user
num_product = int(input("Enter a number: "))

# Find the maximum number in the list
maximum = max(numbers)

# Measure the time it takes to execute the calculation
start_time = time.time()

# Calculate the result
result = num_product * maximum

end_time = time.time()

# Print the result
print("Maximum number in the list:", maximum)
print("Result:", result)

# Calculate and print the execution time
execution_time = end_time - start_time
print("Execution time:", execution_time, "seconds")
