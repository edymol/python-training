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


def find_gcd_slow(a, b):
    gcd = 0
    for d in range(1, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            gcd = d
    return gcd


a = 23456
b = 14567

if max(a, b) < 1000000:  # Choose the slow algorithm for small inputs
    start_time = time.time()
    result = find_gcd_slow(a, b)
    end_time = time.time()
    algorithm_used = "Slow"
else:  # Choose the fast algorithm for larger inputs
    start_time = time.time()
    result = find_gcd_fast(a, b)
    end_time = time.time()
    algorithm_used = "Fast"

execution_time = end_time - start_time
print("GCD:", result)
print(f"Execution time ({algorithm_used} algorithm):", execution_time, "seconds")
