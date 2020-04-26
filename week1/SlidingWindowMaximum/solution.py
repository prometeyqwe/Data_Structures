from sys import stdin


class Queue:
    def __init__(self, size):
        self.size = size
        self.count = 0
        self.res = []
        self.max_list = []
        self.data = []

    def is_full(self):
        return self.size == self.count

    def enqueue(self, value):
        if self.is_full():
            self.dequeue()

        while self.max_list and self.max_list[-1] < value:
            self.max_list.pop(-1)
        self.data.append(value)
        self.max_list.append(value)
        self.count += 1
        if self.is_full():
            self.res.append(int(self.max_list[0]))

    def dequeue(self):
        pop_ = self.data.pop(0)
        self.count -= 1
        if self.max_list[0] == pop_:
            self.max_list.pop(0)


def get_max():
    n = int(stdin.readline().strip())
    data = stdin.readline().strip().split()
    m = int(stdin.readline().strip())
    # m = 1
    # data = [2, 7, 3, 1, 5, 2, 6, 2]  # 27315262
    # data = [1, 2, 5]
    queue = Queue(m)
    for i in data:
        queue.enqueue(int(i))

    return queue.res


if __name__ == '__main__':
    print(*get_max())
