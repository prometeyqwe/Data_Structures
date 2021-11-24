VALUE = 0
LEFT = 1
RIGHT = 2


def in_order(root):
    if data[root][LEFT] != -1:
        in_order(data[root][LEFT])
    print(data[root][VALUE], end=" ")
    if data[root][RIGHT] != -1:
        in_order(data[root][RIGHT])


def pre_order(root):
    print(data[root][VALUE], end=" ")
    if data[root][LEFT] != -1:
        pre_order(data[root][LEFT])
    if data[root][RIGHT] != -1:
        pre_order(data[root][RIGHT])


def post_order(root):
    if data[root][LEFT] != -1:
        post_order(data[root][LEFT])
    if data[root][RIGHT] != -1:
        post_order(data[root][RIGHT])
    print(data[root][VALUE], end=" ")


if __name__ == '__main__':
    # n = int(input())
    # data = []
    # for _ in range(n):
    #     data.append(list(map(int, list(input()))))

    n = 5
    data = [
        [4, 1, 2],
        [2, 3, 4],
        [5, -1, -1],
        [1, -1, -1],
        [3, -1, -1],
    ]
    in_order(0)
    print()
    pre_order(0)
    print()
    post_order(0)

