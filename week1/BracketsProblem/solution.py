from sys import stdin


class Stack:
    def __init__(self):
        self.top = None
        self.data = []
        self.brackets = [")", "}", "]", "(", "{", "["]
        self.allows_brackets = ["()", "{}", "[]"]

    def pop(self):
        if len(self.data) > 1:
            self.top = self.data[-2]
        else:
            self.top = None
        return self.data.pop(-1) if not self.is_empty() else None

    def push(self, value):
        self.data.append(value)
        self.top = value

    def is_empty(self):
        return len(self.data) <= 0


def is_valid(input_text):
    stack = Stack()
    for i in range(len(input_text)):
        if input_text[i] not in stack.brackets:
            continue
        if input_text[i] not in stack.brackets[:3]:
            # (, {, [
            stack.push((input_text[i], i + 1))
        else:
            # ), }, ]
            top = stack.pop()
            if top is None:
                return i + 1
            elif "".join([top[0], input_text[i]]) not in stack.allows_brackets:
                return i + 1
    return "Success" if stack.is_empty() else stack.top[1]


input_string = stdin.readline().strip()
print(is_valid(input_string))
