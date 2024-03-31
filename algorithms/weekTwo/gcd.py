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


a = int(input())
b = int(input())
result = find_gcd_fast(a, b)
print(result)
