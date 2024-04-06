# To avoid rewriting redundant or repetitive code, create a Node class to
# create a Node where is needed
# def __init__(self, value):
# def append(self, value):
# def prepend(self, value):
# def insert(self, value, index):

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        prev = self.head
        while temp.next:
            prev = temp
            temp = temp.next
        self.tail = prev
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp

        after = temp.next
        before = None

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    def find_middle_node(self):
        if not self.head:
            return None
        slow_ptr = self.head
        fast_ptr = self.head
        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        return slow_ptr

    def has_loop(self):
        if not self.head:
            return False
        slow_ptr = self.head
        fast_ptr = self.head
        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
            if slow_ptr == fast_ptr:
                return True
        return False

    def find_kth_from_end(ll, k):
        slow = fast = ll.head
        for _ in range(k):
            if fast is None:
                return None
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next
        return slow

    def partition_list(self, value):
        if not self.head:
            return None

        current = self.head
        lesser_head = lesser_tail = Node(None)  # Dummy nodes for lesser list
        greater_head = greater_tail = Node(None)  # Dummy nodes for greater list

        while current:
            if current.value < value:
                lesser_tail.next = current
                lesser_tail = current
            else:
                greater_tail.next = current
                greater_tail = current
            current = current.next

        lesser_tail.next = greater_head.next  # Combine lesser and greater lists
        greater_tail.next = None  # End the greater list

        self.head = lesser_head.next  # Update the head of the linked list

        return self.head

    def remove_duplicates(self):
        if not self.head:
            return None
        current = self.head
        seen = set()
        prev = None
        while current:
            if current.value in seen:
                prev.next = current.next
                self.length -= 1
            else:
                seen.add(current.value)
                prev = current
            current = current.next  # Move to the next node
        return True


# TEST REMOVE DUPLICATES
def test_remove_duplicates(linked_list, expected_values):
    print("Before: ", end="")
    linked_list.print_list()
    linked_list.remove_duplicates()
    print("After:  ", end="")
    linked_list.print_list()

    # Collect values from linked list after removal
    result_values = []
    node = linked_list.head
    while node:
        result_values.append(node.value)
        node = node.next

    # Determine if the test passes
    if result_values == expected_values:
        print("Test PASS\n")
    else:
        print("Test FAIL\n")


# Test 1: List with no duplicates
ll = LinkedList(1)
ll.append(2)
ll.append(3)
test_remove_duplicates(ll, [1, 2, 3])

# Test 2: List with some duplicates
ll = LinkedList(1)
ll.append(2)
ll.append(1)
ll.append(3)
ll.append(2)
test_remove_duplicates(ll, [1, 2, 3])

# Test 3: List with all duplicates
ll = LinkedList(1)
ll.append(1)
ll.append(1)
test_remove_duplicates(ll, [1])

# Test 4: List with consecutive duplicates
ll = LinkedList(1)
ll.append(1)
ll.append(2)
ll.append(2)
ll.append(3)
test_remove_duplicates(ll, [1, 2, 3])

# Test 5: List with non-consecutive duplicates
ll = LinkedList(1)
ll.append(2)
ll.append(1)
ll.append(3)
ll.append(2)
ll.append(4)
test_remove_duplicates(ll, [1, 2, 3, 4])

# Test 6: List with duplicates at the end
ll = LinkedList(1)
ll.append(2)
ll.append(3)
ll.append(3)
test_remove_duplicates(ll, [1, 2, 3])

# Test 7: Empty list
ll = LinkedList(None)
ll.head = None  # Directly setting the head to None
ll.length = 0  # Adjusting the length to reflect an empty list
test_remove_duplicates(ll, [])

# TEST PARTITION_LIST

# Function to convert linked list to Python list
# def linkedlist_to_list(head):
#     result = []
#     current = head
#     while current:
#         result.append(current.value)
#         current = current.next
#     return result
#
#
# # Function to test partition_list
# def test_partition_list():
#     test_cases_passed = 0
#
#     print("-----------------------")
#
#     # Test 1: Normal Case
#     print("Test 1: Normal Case")
#     x = 3
#     print(f"x = {x}")
#     ll = LinkedList(3)
#     ll.append(1)
#     ll.append(4)
#     ll.append(2)
#     ll.append(5)
#     print("Before:", linkedlist_to_list(ll.head))
#     ll.partition_list(x)
#     print("After:", linkedlist_to_list(ll.head))
#     if linkedlist_to_list(ll.head) == [1, 2, 3, 4, 5]:
#         print("PASS")
#         test_cases_passed += 1
#     else:
#         print("FAIL")
#
#     print("-----------------------")
#
#     # Test 2: All Equal Values
#     print("Test 2: All Equal Values")
#     x = 3
#     print(f"x = {x}")
#     ll = LinkedList(3)
#     ll.append(3)
#     ll.append(3)
#     print("Before:", linkedlist_to_list(ll.head))
#     ll.partition_list(x)
#     print("After:", linkedlist_to_list(ll.head))
#     if linkedlist_to_list(ll.head) == [3, 3, 3]:
#         print("PASS")
#         test_cases_passed += 1
#     else:
#         print("FAIL")
#
#     print("-----------------------")
#
#     # Test 3: Single Element
#     print("Test 3: Single Element")
#     x = 3
#     print(f"x = {x}")
#     ll = LinkedList(1)
#     print("Before:", linkedlist_to_list(ll.head))
#     ll.partition_list(x)
#     print("After:", linkedlist_to_list(ll.head))
#     if linkedlist_to_list(ll.head) == [1]:
#         print("PASS")
#         test_cases_passed += 1
#     else:
#         print("FAIL")
#
#     print("-----------------------")
#
#     # Test 4: Already Sorted
#     print("Test 4: Already Sorted")
#     x = 2
#     print(f"x = {x}")
#     ll = LinkedList(1)
#     ll.append(2)
#     ll.append(3)
#     print("Before:", linkedlist_to_list(ll.head))
#     ll.partition_list(x)
#     print("After:", linkedlist_to_list(ll.head))
#     if linkedlist_to_list(ll.head) == [1, 2, 3]:
#         print("PASS")
#         test_cases_passed += 1
#     else:
#         print("FAIL")
#
#     print("-----------------------")
#
#     # Test 5: Reverse Sorted
#     print("Test 5: Reverse Sorted")
#     x = 2
#     print(f"x = {x}")
#     ll = LinkedList(3)
#     ll.append(2)
#     ll.append(1)
#     print("Before:", linkedlist_to_list(ll.head))
#     ll.partition_list(x)
#     print("After:", linkedlist_to_list(ll.head))
#     if linkedlist_to_list(ll.head) == [1, 3, 2]:
#         print("PASS")
#         test_cases_passed += 1
#     else:
#         print("FAIL")
#
#     print("-----------------------")
#
#     # Test 6: All Smaller Values
#     print("Test 6: All Smaller Values")
#     x = 2
#     print(f"x = {x}")
#     ll = LinkedList(1)
#     ll.append(1)
#     ll.append(1)
#     print("Before:", linkedlist_to_list(ll.head))
#     ll.partition_list(x)
#     print("After:", linkedlist_to_list(ll.head))
#     if linkedlist_to_list(ll.head) == [1, 1, 1]:
#         print("PASS")
#         test_cases_passed += 1
#     else:
#         print("FAIL")
#
#     print("-----------------------")
#
#     # Test 7: Single Element, Equal to Partition
#     print("Test 7: Single Element, Equal to Partition")
#     x = 3
#     print(f"x = {x}")
#     ll = LinkedList(3)
#     print("Before:", linkedlist_to_list(ll.head))
#     ll.partition_list(x)
#     print("After:", linkedlist_to_list(ll.head))
#     if linkedlist_to_list(ll.head) == [3]:
#         print("PASS")
#         test_cases_passed += 1
#     else:
#         print("FAIL")
#
#     print("-----------------------")
#
#     # Summary
#     print(f"{test_cases_passed} out of 7 tests passed.")


# Run the test function
# test_partition_list()

# TEST HAS_LOOP
# my_linked_list_1 = LinkedList(1)
# my_linked_list_1.append(2)
# my_linked_list_1.append(3)
# my_linked_list_1.append(4)
# my_linked_list_1.tail.next = my_linked_list_1.head
# print(my_linked_list_1.has_loop())  # Returns True
#
# my_linked_list_2 = LinkedList(1)
# my_linked_list_2.append(2)
# my_linked_list_2.append(3)
# my_linked_list_2.append(4)
# print(my_linked_list_2.has_loop())  # Returns False

# TEST REVERSE
# my_linked_list = LinkedList(1)
# my_linked_list.append(2)
# my_linked_list.append(3)
# my_linked_list.append(4)
#
# print('LL before reverse():')
# my_linked_list.print_list()
#
# my_linked_list.reverse()
#
# print('\nLL after reverse():')
# my_linked_list.print_list()
#
# print('\nmiddle value')
# print(my_linked_list.find_middle_node().value)

# TEST REMOVE
# my_linked_list = LinkedList(1)
# my_linked_list.append(2)
# my_linked_list.append(3)
# my_linked_list.append(4)
# my_linked_list.append(5)
#
# print('LL before remove():')
# my_linked_list.print_list()
#
# print('\nRemoved node:')
# print(my_linked_list.remove(2).value)
# print('LL after remove() in middle:')
# my_linked_list.print_list()
#
# print('\nRemoved node:')
# print(my_linked_list.remove(0).value)
# print('LL after remove() of first node:')
# my_linked_list.print_list()
#
# print('\nRemoved node:')
# print(my_linked_list.remove(2).value)
# print('LL after remove() of last node:')
# my_linked_list.print_list()

# TEST INSERT
# my_linked_list = LinkedList(1)
# my_linked_list.append(3)
#
#
# print('LL before insert():')
# my_linked_list.print_list()
#
#
# my_linked_list.insert(1,2)
#
# print('\nLL after insert(2) in middle:')
# my_linked_list.print_list()
#
#
# my_linked_list.insert(0,0)
#
# print('\nLL after insert(0) at beginning:')
# my_linked_list.print_list()
#
#
# my_linked_list.insert(4,4)
#
# print('\nLL after insert(4) at end:')
# my_linked_list.print_list()
