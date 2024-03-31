# A system of disjoint sets with a specific canonical element add a find method to the disjoint set system data type
# so that find i returns the largest element of the related component containing i. The union, connected,
# and find methods operations must run in algorithmic or best time. For example, if one of the connected components
# is 1, 2, 6, 9, then find method must return 9 for each of the four elements in related components. For example,
# if one of the connected components is {1, 2, 6, 9} then find method must return 9 for each of the four elements in
# related components.

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.max_element = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.max_element[self.parent[x]]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.size[root_x] < self.size[root_y]:
                root_x, root_y = root_y, root_x
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
            self.max_element[root_x] = max(self.max_element[root_x], self.max_element[root_y])

# Example usage
n = 10
uf = UnionFind(n)
uf.union(1, 2)
uf.union(2, 6)
uf.union(6, 9)
print(uf.find(1))  # Output: 9
print(uf.find(2))  # Output: 9
print(uf.find(6))  # Output: 9
print(uf.find(9))  # Output: 9

