VALUE = 0
LEFT = 1
RIGHT = 2


def is_left_ok(node, value):
    result = True
    if not data[node][VALUE] < value:
        return False

    if data[node][LEFT] != -1:
        result = is_left_ok(data[node][LEFT], value)

    if result and data[node][RIGHT] != -1:
        result = is_left_ok(data[node][LEFT], value)

    return result


def is_right_ok(node, value):
    result = True
    if not data[node][VALUE] > value:
        return False

    if data[node][LEFT] != -1:
        result = is_right_ok(data[node][LEFT], value)

    if result and data[node][RIGHT] != -1:
        result = is_right_ok(data[node][RIGHT], value)

    return result


def check_tree_property(root):
    left = data[root][LEFT]
    right = data[root][RIGHT]
    result = True

    if left != -1:
        result = is_left_ok(left, data[root][VALUE])
    if result and right != -1:
        result = is_right_ok(right, data[root][VALUE])

    return result


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

    for i in range(n):
        if not check_tree_property(i):
            print("INCORRECT")
            break
    else:
        print("CORRECT")
