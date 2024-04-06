class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack(object):
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1

    def pop(self):
        if self.height == 0:
            return None
        else:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            self.height -= 1
        return temp

# TEST POP
my_stack = Stack(4)
my_stack.push(3)
my_stack.push(2)
my_stack.push(1)

print('Stack before pop():')
my_stack.print_stack()

print('\nPopped node:')
print(my_stack.pop().value)

print('\nStack after pop():')
my_stack.print_stack()

# TEST PUSH
# my_stack = Stack(2)
#
# print('Stack before push(1):')
# my_stack.print_stack()
#
# my_stack.push(1)
#
# print('\nStack after push(1):')
# my_stack.print_stack()


# TEST STACK
# my_stack = Stack(5)
# my_stack.print_stack()
