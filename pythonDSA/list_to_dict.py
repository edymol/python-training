def list_to_dict(lst):
    return {item: lst.count(item) for item in lst}


# Example usage:
my_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
result_dict = list_to_dict(my_list)
print(result_dict)
