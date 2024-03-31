def find_lcm(x, y):
    # Find the greater number
    if x > y:
        greater = x
    else:
        greater = y

    while True:
        if (greater % x == 0) and (greater % y == 0):
            lcm = greater
            break
        greater += 1

    return lcm


# Example usage:
num1 = int(input())
num2 = int(input())
lcm = find_lcm(num1, num2)
# print("The least common multiple of", num1, "and", num2, "is", lcm)
print(lcm)
