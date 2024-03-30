# How would you design a stack which, in addition to push and pop, has a function min
# which returns the minimum element? Push, pop and min should all operate in 0(1) time.

class MinStack:
    def __init__(self):
        self.stack = []  # Main stack to store elements
        self.min_stack = []  # Auxiliary stack to store minimum elements

    def push(self, x):
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self):
        if self.stack:
            popped = self.stack.pop()
            if popped == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1]
        return None

    def get_min(self):
        if self.min_stack:
            return self.min_stack[-1]
        return None


# Example usage:
stack = MinStack()
stack.push(3)
stack.push(5)
stack.push(2)
stack.push(1)

print("Minimum element:", stack.get_min())  # Output: 1

stack.pop()
print("Minimum element after pop:", stack.get_min())  # Output: 2
