class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp:
            print(temp.value)
            temp = temp.next

    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp

# TEST DEQUEUE
my_queue = Queue(1)
my_queue.enqueue(2)

# (2) Items - Returns 2 Node
print(my_queue.dequeue().value)
# (1) Item -  Returns 1 Node
print(my_queue.dequeue().value)
# (0) Items - Returns None
print(my_queue.dequeue())


# TEST ENQUEUE
# my_queue = Queue(1)
#
# print('Queue before enqueue(2):')
# my_queue.print_queue()
#
# my_queue.enqueue(2)
#
# print('\nQueue after enqueue(2):')
# my_queue.print_queue()

# TEST QUEUE CONSTRUCTOR
# my_queue = Queue(4)
#
# print('First:', my_queue.first.value)
# print('Last:', my_queue.last.value)
# print('Length:', my_queue.length)