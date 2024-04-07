# Set: Has Unique Chars ( ** Interview Question) Write a function called has_unique_chars that takes a string as
# input and returns True if all the characters in the string are unique, and False otherwise.
# For example, has_unique_chars('abcdefg') should return True, while has_unique_chars('hello') should return False.

# Naive way with O(nˆ2)
def has_unique_chars(lst):
    seen = []
    for i in lst:
        if i in seen:
            return False
        seen.append(i)
    return True


# Efficient way with O(1)
def has_unique_chars_efficient(lst):
    seen = set()
    for i in lst:
        if i in seen:
            return False
        seen.add(i)
    return True


print(has_unique_chars('abcdefg'))  # should return True
print(has_unique_chars('hello'))  # should return False
print(has_unique_chars(''))  # should return True
print(has_unique_chars('0123456789'))  # should return True
print(has_unique_chars('abacadaeaf'))  # should return False


# Set: Find Pairs ( ** Interview Question) You are given two lists of integers, arr1 and arr2, and a target integer
# value, target. Your task is to find all pairs of numbers (one from arr1 and one from arr2) whose sum equals target.
# Write a function called find_pairs that takes in three arguments: arr1, arr2, and target, and returns a list of all
# such pairs.  Assume that each array does not contain duplicate values.

# Naive approach with O(nˆ2)
def find_pairs(arr1, arr2, target):
    pairs = []
    for num1 in arr1:
        for num2 in arr2:
            if num1 + num2 == target:
                pairs.append((num1, num2))
    return pairs


# efficient approach with O(n)
def find_pairs_efficient(arr3, arr4, target1):
    pairs1 = []
    set_arr3 = set(arr3)
    for num in arr4:
        complement = target1 - num
        if complement in set_arr3:
            pairs1.append((complement, num))
    return pairs


# Test case
arr3 = [1, 2, 3, 4, 5]
arr4 = [2, 4, 6, 8, 10]
target1 = 7

pairs1 = find_pairs(arr3, arr4, target1)
print (pairs1)

arr1 = [1, 2, 3]
arr2 = [4, 5, 6]
target = 9
pairs = find_pairs(arr1, arr2, target)
print(pairs)
