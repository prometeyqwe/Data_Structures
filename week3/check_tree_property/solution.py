def check_tree_property(root, _from, _to):
    if _from < data[root][0] < _to:
        left_res = check_tree_property(data[root][1], _from, data[root][0]) if data[root][1] != -1 else True
        if left_res:
            right_res = check_tree_property(data[root][2], data[root][0], _to) if data[root][2] != -1 else True
        else:
            right_res = False
        res = left_res and right_res
    else:
        res = False

    return res


if __name__ == '__main__':
    n = int(input())
    data = []
    for _ in range(n):
        data.append(list(map(int, list(input()))))

    # CORRECT
    # n = 5
    # data = [
    #     [4, 1, 2],
    #     [2, 3, 4],
    #     [5, -1, -1],
    #     [1, -1, -1],
    #     [3, -1, -1],
    # ]

    # INCORRECT
    # n = 3
    # data = [
    #     [1, 1, 2],
    #     [2, -1, -1],
    #     [3, -1, -1],
    # ]

    # INCORRECT
    # n = 4
    # data = [
    #     [2, -1, 1],
    #     [5, 2, -1],
    #     [3, -1, 3],
    #     [5, -1, -1],
    # ]
    if data:
        if check_tree_property(0, float("-inf"), float("inf")):
            print("CORRECT")
        else:
            print("INCORRECT")
    else:
        print("CORRECT")

