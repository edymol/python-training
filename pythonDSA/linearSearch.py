array_to_search = [i for i in range(0, 50)]
value_to_search = 60


def linear_search(array, value):
    try:
        index = array.index(value)
        return index
    except ValueError:
        return -1


result = linear_search(array_to_search, value_to_search)
print(result)

# leftSide = 0
# rightSide = len(array_to_search)
value_to_search = 13


