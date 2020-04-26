from sys import stdin


class Stack:
    def __init__(self):
        self.data = []
        self.max_stack = []

    def push(self, value):
        self.data.append(value)
        if not self.max_stack:
            self.max_stack.append(value)
        else:
            self.max_stack.append(max(self.max_stack[-1], value))

    def pop(self):
        self.max_stack.pop(-1)
        return self.data.pop(-1)

    def max_(self):
        return self.max_stack[-1]


if __name__ == '__main__':
    stack = Stack()
    n = int(stdin.readline().strip())
    for i in range(n):
        command = stdin.readline().strip().split()
        if command[0] == "push":
            stack.push(int(command[1]))
        elif command[0] == "pop":
            stack.pop()
        else:
            print(stack.max_())


