import sys
import time
from sys import stdin

sys.setrecursionlimit(1000000)


def get_height(nodes, root_value, height, mapping):
    if not mapping:
        mapping = dict()
        mapping["-1"] = [str(nodes.index("-1"))]
        for i in range(len(nodes)):
            for j in range(len(nodes)):
                if str(i) == nodes[j]:
                    if mapping.get(str(i)):
                        mapping[str(i)].append(str(j))
                    else:
                        mapping[str(i)] = [str(j)]

    if int(root_value) >= 0:
        height += 1
    roots = mapping.get(root_value, [])
    if roots:
        result = []
        for r in roots:
            result.append(get_height(nodes, r, height, mapping))
        height = max(result)
    return height


def get_height1(nodes):

    # childs = [i for i in range(len(nodes)) if i not in nodes]
    max_hight = 0
    hight = 0
    for i in nodes:
        val = i
        while val != "-1":
            val = nodes[int(val)]
            hight += 1
        max_hight = max(hight, max_hight)
        hight = 0

    return max_hight


def get_height2(nodes, n):
    map1 = dict()
    map1["-1"] = 0

    for i in range(int(n)):
        if str(i) not in map1:
            h = 1 + rec(nodes, nodes[i], map1)
            map1[str(i)] = h
    return max(map1.values())


def rec(nodes, node, map1):
    if node not in map1:
        h = rec(nodes, nodes[int(node)], map1)
        map1[node] = 1 + h
        return map1[node]
    else:
        return map1[node]


# 5
# 4 -1 4 1 1

# n = stdin.readline().strip()
# nodes = stdin.readline().strip().split()
# print(get_height2(nodes, n))
n = 10 ** 3
nodes = [i+1 for i in range(n-1)] + [-1]
print((get_height2(nodes, n)))
