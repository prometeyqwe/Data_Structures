class DisjointSets:
    """ Непересекающиеся множества """

    def __init__(self, n, rank=None):
        self.parents = [i for i in range(n)]
        self.rank = rank or [1] * n

    def union_sets(self, dest, src):
        dest_root = self.find(dest - 1)
        src_root = self.find(src - 1)

        if dest_root != src_root:
            # change parent for src root
            self.parents[src_root] = dest_root
            self.rank[dest_root] += self.rank[src_root]

    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]


if __name__ == "__main__":
    # n, e, d = map(int, input().split())
    n, e, d = 4, 0, 6
    disjoint_sets = DisjointSets(n)

    x_y = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4), (1, 2)]

    # for _ in range(e):
    #     x, y = map(int, input().split())
    #     disjoint_sets.union_sets(x, y)
    
    for x, y in x_y[:e]:
        print(x, y)
        disjoint_sets.union_sets(x, y)

    # for _ in range(d):
    #     x, y = map(int, input().split())
    #     if disjoint_sets.find(x - 1) != disjoint_sets.find(y - 1):
    #         break
    # else:
    #     print(1)
    # print(0)
    print("===")
    result = 0
    if d:
        for x, y in x_y[e:]:
            print(x, y)
            if disjoint_sets.find(x - 1) == disjoint_sets.find(y - 1):
                break
        else:
            result = 1
    else:
        result = 1
    print(result)
    