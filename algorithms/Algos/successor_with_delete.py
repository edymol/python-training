class Node:
    def __init__(self, val, index):
        self.val = val
        self.index = index
        self.left = None
        self.right = None
        self.parent = None
        self.size = 1
        self.color = 'RED'


class RedBlackTree:
    def __init__(self):
        self.root = None

    def insert(self, val, index):
        node = Node(val, index)
        if not self.root:
            self.root = node
        else:
            curr = self.root
            while curr:
                if val < curr.val:
                    if curr.left:
                        curr = curr.left
                    else:
                        curr.left = node
                        node.parent = curr
                        break
                else:
                    if curr.right:
                        curr = curr.right
                    else:
                        curr.right = node
                        node.parent = curr
                        break
            while curr:
                curr.size += 1
                curr = curr.parent
            self._balance(node)

    def remove(self, val):
        node = self._find(val)
        if not node:
            return False
        self._delete_node(node)
        return True

    def next_element(self, val):
        curr = self.root
        next_val = None
        while curr:
            if val < curr.val:
                next_val = curr.val
                curr = curr.left
            else:
                curr = curr.right
        return next_val

    def _find(self, val):
        curr = self.root
        while curr:
            if val == curr.val:
                return curr
            elif val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        return None

    def _delete_node(self, node):
        if not node.left or not node.right:
            y = node
        else:
            y = self._successor(node)
        if y.left:
            x = y.left
        else:
            x = y.right
        if x:
            x.parent = y.parent
        if not y.parent:
            self.root = x
        elif y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x
        if y != node:
            node.val = y.val
        curr = y.parent
        while curr:
            curr.size -= 1
            curr = curr.parent
        self._balance_delete(x, y.parent)

    def _balance(self, node):
        while node != self.root and node.parent and node.parent.color == 'RED':
            parent = node.parent
            grandparent = parent.parent

            if grandparent:
                if grandparent.left == parent:
                    uncle = grandparent.right
                    if uncle and uncle.color == 'RED':
                        parent.color = 'BLACK'
                        uncle.color = 'BLACK'
                        grandparent.color = 'RED'
                        node = grandparent
                    else:
                        if parent.right == node:
                            node = parent
                            if node.parent:
                                self._left_rotate(node)
                                parent = node.parent
                        parent.color = 'BLACK'
                        if grandparent:
                            grandparent.color = 'RED'
                            if grandparent.left:
                                if grandparent.left == parent:
                                    self._right_rotate(grandparent)
                else:
                    uncle = grandparent.left
                    if uncle and uncle.color == 'RED':
                        parent.color = 'BLACK'
                        uncle.color = 'BLACK'
                        grandparent.color = 'RED'
                        node = grandparent
                    else:
                        if parent.left == node:
                            node = parent
                            if node.parent:
                                self._right_rotate(node)
                                parent = node.parent
                        parent.color = 'BLACK'
                        if grandparent:
                            grandparent.color = 'RED'
                            if grandparent.right:
                                if grandparent.right == parent:
                                    self._left_rotate(grandparent)
            else:
                break
        self.root.color = 'BLACK'

    def _balance_delete(self, x, parent):
        while x != self.root and (not x or x.color == 'BLACK'):
            if x == parent.left:
                sibling = parent.right
                if sibling:
                    if sibling.color == 'RED':
                        sibling.color = 'BLACK'
                        parent.color = 'RED'
                        self._left_rotate(parent)
                        sibling = parent.right
                    if sibling and ((not sibling.left or sibling.left.color == 'BLACK') and \
                                    (not sibling.right or sibling.right.color == 'BLACK')):
                        sibling.color = 'RED'
                        x = parent
                        parent = x.parent
                    else:
                        if sibling.right and sibling.right.color == 'BLACK':
                            sibling.left.color = 'BLACK'
                            sibling.color = 'RED'
                            self._right_rotate(sibling)
                            sibling = parent.right
                        if sibling:
                            sibling.color = parent.color
                            parent.color = 'BLACK'
                            if sibling.right:
                                sibling.right.color = 'BLACK'
                            self._left_rotate(parent)
                        x = self.root
                else:
                    sibling = Node(None)  # Create a dummy node for sibling
                    sibling.color = 'BLACK'  # Set color to black for dummy node
                    sibling.parent = parent  # Set parent reference for dummy node
                    parent.right = sibling  # Assign dummy node as sibling
            else:
                sibling = parent.left
                if sibling:
                    if sibling.color == 'RED':
                        sibling.color = 'BLACK'
                        parent.color = 'RED'
                        self._right_rotate(parent)
                        sibling = parent.left
                    if sibling and ((not sibling.right or sibling.right.color == 'BLACK') and \
                                    (not sibling.left or sibling.left.color == 'BLACK')):
                        sibling.color = 'RED'
                        x = parent
                        parent = x.parent
                    else:
                        if sibling.left and sibling.left.color == 'BLACK':
                            sibling.right.color = 'BLACK'
                            sibling.color = 'RED'
                            self._left_rotate(sibling)
                            sibling = parent.left
                        if sibling:
                            sibling.color = parent.color
                            parent.color = 'BLACK'
                            if sibling.left:
                                sibling.left.color = 'BLACK'
                            self._right_rotate(parent)
                        x = self.root
                else:
                    sibling = Node(None)  # Create a dummy node for sibling
                    sibling.color = 'BLACK'  # Set color to black for dummy node
                    sibling.parent = parent  # Set parent reference for dummy node
                    parent.left = sibling  # Assign dummy node as sibling
        if x:
            x.color = 'BLACK'

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left:
            y.left.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right:
            x.right.parent = y
        x.parent = y.parent
        if not y.parent:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x


class ElementRemovalDataStructure:
    def __init__(self, elements):
        self.tree = RedBlackTree()
        self.index_map = {}
        for i, element in enumerate(elements):
            self.tree.insert(element, i)
            self.index_map[i] = element

    def remove(self, index):
        element = self.index_map[index]
        del self.index_map[index]
        return self.tree.remove(element)

    def next_element(self, element):
        return self.tree.next_element(element)


# Example usage
elements = [3, 1, 4, 6, 2, 5]
ds = ElementRemovalDataStructure(elements)
print(ds.next_element(3))  # Output: 4
print(ds.remove(2))         # Output: True
print(ds.next_element(4))  # Output: 5
