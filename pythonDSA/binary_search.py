array_to_search = [i for i in range(0, 50)]
value_to_search = 13


# def binary_search(array, value, left_side=0, right_side=len(array_to_search) - 1):
#     # if right_side is None:
#     #     right_side = len(array) - 1
#     while left_side <= right_side:
#         midpoint = (left_side + right_side) // 2
#         if array[midpoint] == value:
#             return midpoint
#         elif array[midpoint] > value:
#             right_side = midpoint - 1
#         else:
#             left_side = midpoint + 1
#
#     return -1  # Return -1 if value is not found

def binary_search(array, value):
    if not array:
        return False
    midpoint = len(array) // 2
    if array[midpoint] == value:
        return value
    elif array[midpoint] > value:
        return binary_search(array[:midpoint], value)
    else:
        return binary_search(array[midpoint + 1:], value)


result = binary_search(array_to_search, value_to_search)
print(result)
