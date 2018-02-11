class OptimizedUnionFind:
    def __init__(self, num_node):
        self.parent = [i for i in range(num_node)]
        self.rank = [0 for i in range(num_node)]
        self.size = [1 for i in range(num_node)]
        self.num_set = num_node

    def size_of(self, u):
        return self.size[u]

    def find(self, u):
        if self.parent[u] == u:
            return u

        self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def merge(self, u, v):
        u = self.find(u)
        v = self.find(v)

        if u != v:
            if self.rank[u] > self.rank[v]:
                u, v = v, u

            self.parent[u] = v
            self.size[v] += self.size[u]
            if self.rank[u] == self.rank[v]:
                self.rank[v] += 1

            self.num_set -= 1