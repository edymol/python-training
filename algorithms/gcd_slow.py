import time


def find_gcd_slow(a, b):
    gcd = 0  # Initialize gcd variable
    for d in range(1, min(a, b) + 1):  # Range should be up to the minimum of a and b
        if a % d == 0 and b % d == 0:
            gcd = d  # Update gcd if d is a common divisor
    return gcd


start_time = time.time()
result = find_gcd_slow(3918848, 1653264)
end_time = time.time()
# Call the function and print the result
result = find_gcd_slow(3918848, 1653264)
print("GCD:", result)
