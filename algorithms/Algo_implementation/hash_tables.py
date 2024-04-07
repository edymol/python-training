class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            # The calculation below is to find the address space from 0 to 6
            # my_hash + ord(letter) gets the ASCII of the letter and multiplies to a prime number
            # the % len(self.data_map) which is 7 will give the reminder of that multiplication and
            # will be anywhere from 0 to 6 address
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def print_table(self):
        for i, value in enumerate(self.data_map):
            print(i, ": ", value)

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None

    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:  # this will ensure the loop only runs if index is not empty
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys


# Naive approach to find the common item in two lists O(nˆ2)
def item_in_common(list1, list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False


# Recommend approach with a O(n) time complexity
def item_in_common2(list3, list4):
    my_dict = {}
    for i in list3:
        my_dict[i] = True
    for j in list4:
        if j in my_dict:
            return True
    return False


# Convert a list to a dictionary with key as the item and value as the count of the item
my_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

# Convert list to dictionary with counts
my_dict = {item: my_list.count(item) for item in my_list}

print(my_dict)

list3 = ['1', '2', '3', '4', 'e', 'f', 'g', 'h']
list4 = ['6', '7', '8', '9', 'a', 'b', 'c', 'd']
print(item_in_common2(list3, list4))

list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
list2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(item_in_common(list1, list2))

# TEST KEYS METHOD
# my_hash_table = HashTable()
#
# my_hash_table.set_item('bolts', 1400)
# my_hash_table.set_item('washers', 50)
# my_hash_table.set_item('lumber', 70)
#
# print(my_hash_table.keys())

# TEST GET ITEM
# my_hash_table = HashTable()
#
# my_hash_table.set_item('bolts', 1400)
# my_hash_table.set_item('washers', 50)
#
# print('Bolts:', my_hash_table.get_item('bolts'))
# print('Washers:', my_hash_table.get_item('washers'))
# print('Lumber:', my_hash_table.get_item('lumber'))

# TEST SET ITEM
# my_hash_table = HashTable()
#
# my_hash_table.set_item('bolts', 1400)
# my_hash_table.set_item('washers', 50)
# my_hash_table.set_item('lumber', 70)
#
# my_hash_table.print_table()

# TEST HASH TABLE CONSTRUCTOR
# my_hash_table = HashTable()
# my_hash_table.print_table()
