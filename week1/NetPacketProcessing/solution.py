from sys import stdin


class MyQueue:
    def __init__(self, size):
        self.size = int(size)
        self.count = 0
        self.data = []
        self.tail = 0
        self.top = None

    def is_full(self):
        return self.size == self.count

    def enqueue(self, value):
        if self.is_full() and self.top <= value[0]:
            self.dequeue()

        if not self.is_full():
            self.count += 1
            res = max(self.tail, value[0])
            self.data.append(value[1] + res)
            self.top = self.data[0]
            self.tail = self.data[-1]
            return int(res)
        else:
            return -1

    def dequeue(self):
        self.count -= 1
        self.data.pop(0)
        if self.count:
            self.top = self.data[0]
        else:
            self.top = None
            self.tail = 0


def process_time(buffer_size, data):
    queue = MyQueue(buffer_size)
    res = []
    for i in data:
        res.append(queue.enqueue(i))

    return res


if __name__ == '__main__':
    size, n = stdin.readline().strip().split()
    data = []
    for i in range(int(n)):
        arrival, duration = stdin.readline().strip().split()
        data.append([float(arrival), float(duration)])

    print(*process_time(size, data), sep="\n") if n else ""


