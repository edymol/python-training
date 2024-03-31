import inspect
import time

# compute = int(input("Enter the number to compute: "))
compute = int(input())


def fib_faster(n):
    if n <= 1:
        return n

    fib = [0, 1]

    for i in range(2, n + 1):  # Corrected the loop range
        fib.append(fib[i - 1] + fib[i - 2])

    return fib[-1]  # Return the last element of the Fibonacci sequence


# start_time = time.time()  # Start measuring time
result = fib_faster(compute)
# end_time = time.time()  # End measuring time
# execution_time = end_time - start_time  # Calculate execution time
# lines_of_code = len(inspect.getsource(fib_faster).split('\n'))
# print("Number of lines in fib_faster:", lines_of_code)
#
print("Result:", result)
# print("Execution time:", execution_time, "seconds")
