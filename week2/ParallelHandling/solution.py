from sys import stdin
from week2.Heap.solution import MinHeap


class MyMinHeap(MinHeap):
    def change_priority(self, index, new_priority):
        old_priority = self.data[index]
        t = old_priority // self.size
        process_count = old_priority % self.size

        self.data[index] = (t + new_priority) * self.size + process_count
        if self.data[index] > old_priority:
            self.sift_down(index)
        else:
            self.sift_up(index)


def parallel_handling(handlers_count, tasks_count, task_times):
    priorityQueue = MyMinHeap(handlers_count)
    for _ in range(handlers_count):
        priorityQueue.insert_into(_)
    for task_number in range(tasks_count):
        print(priorityQueue.get_min() % priorityQueue.size, priorityQueue.get_min() // priorityQueue.size)
        priorityQueue.change_priority(0, task_times[task_number])


if __name__ == '__main__':
    n, m = map(int, stdin.readline().strip().split())
    times_array = list(map(int, stdin.readline().split()))
    # n = 2
    # m = 5
    # times_array = [1, 2, 3, 4, 5]
    # print(n)
    # print(m)
    # print(times_array)

    parallel_handling(n, m, times_array)

