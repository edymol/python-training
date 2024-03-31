# Interaction through a social network. Given a social network with n participants and a log file containing m
# timestamps with the time of friendship formation between pairs of participants. Create an algorithm to determine
# the earliest time a connection between all participants will form (that is, when each participant becomes a friend
# of another participant who is a friend of another participant, etc.). It is assumed that the log file is sorted by
# timestamps and that friendship between participants is expressed through an equivalence relation. The execution
# time of your algorithm should be logmlogn or better, and the additional memory space used should be proportional to
# n. Note: These interview questions are not graded and are designed to improve your skills. To get a hint,
# submit a solution.

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.sets = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.size[root_x] < self.size[root_y]:
                root_x, root_y = root_y, root_x
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
            self.sets -= 1


def earliest_connection_time(n, log):
    uf = UnionFind(n)
    for time, u, v in log:
        uf.union(u, v)
        if uf.sets == 1:
            return time
    return -1  # No connection formed among all participants


# Example usage
n = 4
log = [(1, 0, 1), (2, 1, 2), (3, 2, 3)]
print(earliest_connection_time(n, log))  # Output: 3
