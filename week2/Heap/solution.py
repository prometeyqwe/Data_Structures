class MinHeap:
    def __init__(self, size, data=None):
        self.size = 0
        self.max_size = size
        self.data = data or []
        if self.data:
            self.size = len(self.data)
        self.swap_storage = []

    def insert_into(self, value):
        self.data.append(value)
        self.size += 1
        self.sift_up(self.size - 1)

    def extract_min(self):
        self.swap(0, self.size-1)
        print("extract_min::swap_result: {0}".format(self.data))
        _min = self.data.pop(self.size-1)
        self.size -= 1
        self.sift_down(0)

        return _min

    def sift_down(self, index):
        min_index = index
        left_child_index = self._get_left_child(index)
        right_child_index = self._get_right_child(index)
        if left_child_index < self.size and self.data[index] > self.data[left_child_index]:
            min_index = left_child_index
        if right_child_index < self.size and self.data[index] > self.data[right_child_index] and self.data[right_child_index] < self.data[left_child_index]:
            min_index = right_child_index

        if min_index != index:
            self.swap(index, min_index)
            self.sift_down(min_index)

    def sift_up(self, index):
        if index:
            parent_index = self._get_parent(index)
            if self.data[index] < self.data[parent_index]:
                self.swap(index, parent_index)
                self.sift_up(parent_index)

    def change_priority(self, index, new_priority):
        old_priority = self.data[index]
        self.data[index] = new_priority
        if new_priority > old_priority:
            self.sift_down(index)
        else:
            self.sift_up(index)

    def get_min(self):
        return self.data[0] if self.data else None

    def remove(self, index):
        self.change_priority(index, self.get_min() - 1)
        self.extract_min()

    @staticmethod
    def _get_parent(index):
        return (index - 1) // 2

    @staticmethod
    def _get_left_child(index):
        return 2 * index + 1

    @staticmethod
    def _get_right_child(index):
        return 2 * index + 2

    def swap(self, i, j):
        temp = self.data[i]
        self.data[i] = self.data[j]
        self.data[j] = temp
        self.swap_storage.append((i, j))

    def heap_sort(self):
        for _ in range(len(self.data)):
            self.swap(0, self.size - 1)
            self.size -= 1
            self.sift_down(0)


def build_heap(input_arr, arr_len):
    my_heap2 = MinHeap(arr_len, data=input_arr)
    for i in range(my_heap2.size // 2, -1, -1):
        # print(i + 1)
        my_heap2.sift_up(i)
    print(len(my_heap2.swap_storage))
    for i in my_heap2.swap_storage:
        print(*i)

    print(my_heap2.data)


if __name__ == '__main__':
    # n = int(stdin.readline().strip())
    # n = 6
    # input_array = list(map(int, stdin.readline().split()))
    # input_array = [5, 4, 3, 2, 1]
    # input_array = [1, 2, 3, 4, 5]
    # build_heap(input_array, n)
    my_heap = MinHeap(5)
    my_heap.insert_into(1)
    my_heap.insert_into(2)
    my_heap.insert_into(5)
    my_heap.insert_into(3)
    my_heap.insert_into(4)
    print(my_heap.data)
    my_heap.heap_sort()
    print(my_heap.data)
