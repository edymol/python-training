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

# TEST HASH TABLE CONSTRUCTOR
my_hash_table = HashTable()
my_hash_table.print_table()