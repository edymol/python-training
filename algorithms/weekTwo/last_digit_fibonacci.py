def last_digit_fibonacci(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(2, n + 1):
        previous, current = current % 10, (previous + current) % 10

    return current


# Example usage:
# n = int(input("Enter the value of n: "))
n = int(input())
result = last_digit_fibonacci(n)
# nprint("Last digit of Fibonacci number at position", n, "is:", result)
print(result)