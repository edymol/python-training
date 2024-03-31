import time


def prime_factorization(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors


def find_gcd_fast(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# Call the function and print the result
# start_time = time.time()
# result = find_gcd_fast(2345678955, 2345678955)
# end_time = time.time()

# print("GCD:", result)
# print("Execution time:", end_time - start_time, "seconds")

# Input numbers
a = 35
b = 234567

# Measure execution time
start_time = time.time()
result = find_gcd_fast(a, b)
end_time = time.time()

# Calculate and print execution time
execution_time = end_time - start_time
print("GCD:", result)
print("Execution time fast:", execution_time, "seconds")


def find_gcd_slow(a, b):
    gcd = 0  # Initialize gcd variable
    for d in range(1, min(a, b) + 1):  # Range should be up to the minimum of a and b
        if a % d == 0 and b % d == 0:
            gcd = d  # Update gcd if d is a common divisor
    return gcd


start_time = time.time()
result = find_gcd_slow(a, b)
end_time = time.time()
# Call the function and print the result
execution_time = end_time - start_time
print("GCD:", result)
print("Execution time slow:", execution_time, "seconds")
