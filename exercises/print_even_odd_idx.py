# Task
# Given a string, S, of length N that is indexed from 0 to N-1 , print its even-indexed and odd-indexed characters as
# space-separated strings on a single line (see the Sample below for more detail).
#
# Note: 0 is considered to be an even index.
#
# Example
# s = adbecf
# Print abc def
#
# Input Format
#
# The first line contains an integer, T (the number of test cases).
# Each line i of the T subsequent lines contain a string, S.
#
# Constraints
# 1≤T≤10: The number of test cases.
# 2 ≤ length of 𝑆 ≤ 10000
# Output Format
# For each String Sj (where 0 ≤ 𝑗 ≤ 𝑇 − 1), print Sj's even-index characters.
# For each String  (where ), print 's even-indexed characters, followed by a space, followed by 's odd-indexed
# characters.
#

# Define the number of strings
T = int(input())

# Iterate through each string
for _ in range(T):
    # Input a string
    s = input()

    even = ''
    odd = ''

    # Iterate through each character in the string
    for i, char in enumerate(s):
        # Check if the index is even or odd
        if i % 2 == 0:
            # Add even-indexed characters to the 'even' string
            even += char
        else:
            # Add odd-indexed characters to the 'odd' string
            odd += char

    # Print the concatenated even and odd-indexed characters with a space in between
    print(even, odd)
