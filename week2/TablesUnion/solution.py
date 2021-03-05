class DisjointSets:
    """ Непересекающиеся множества """

    def __init__(self, n, rank):
        self.parents = [i for i in range(n)]
        self.rank = rank
        self.max_complexity = max(self.rank)

    def union_sets(self, dest, src):
        dest_root = self.find(dest - 1)
        src_root = self.find(src - 1)

        if dest_root != src_root:
            # change parent for src root
            self.parents[src_root] = dest_root
            self.rank[dest_root] += self.rank[src_root]
            if self.rank[dest_root] > self.max_complexity:
                self.max_complexity = self.rank[dest_root]

    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]


if __name__ == "__main__":
    # n, m = map(int, input().split())
    n, m = 5, 5

    # rank = list(map(int, input().split()))
    rank = [1, 1, 1, 1, 1]

    # dest_src = []
    # for _ in range(m):
    #     dest, src = map(int, input().split())
    #     dest_src.append((dest, src))

    dest_src = [(3, 5), (2, 4), (1, 4), (5, 4), (5, 3)]

    disjoint_sets = DisjointSets(n, rank)

    for dest, src in dest_src:
        disjoint_sets.union_sets(dest, src)
        print(disjoint_sets.max_complexity)
