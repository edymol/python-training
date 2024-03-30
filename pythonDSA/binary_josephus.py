def binary_josephus(n):
    return (n ^ (1 << (n.bit_length() - 1))) << 1


# Example usage
n = 10
print("Position of the last remaining person:", binary_josephus(n))
