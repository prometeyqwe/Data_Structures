from collections import deque


class ChainHash():
    def __init__(self, size):
        self.hash_table = [deque() for _ in range(size)]
        self.size = size
        self.handler_dict = {
            "find": self.find_string,
            "add": self.add_string,
            "del": self.del_string,
            "check": self.check_i
        }
        self.p = 1_000_000_007
        self.x = 263
        self.x_pow = [0] * 15
        self.x_pow[0] = 1
        for i in range(1, 15):
            self.x_pow[i] = (self.x_pow[i-1] * self.x) % self.p

    def add_string(self, _string):
        string_hash = self._hash(_string)
        if not self.hash_table[string_hash]:
            self.hash_table[string_hash].appendleft((_string))
        else:
            for _str in self.hash_table[string_hash]:
                if _str == _string:
                    break
            else:
                self.hash_table[string_hash].appendleft((_string))

    def del_string(self, _string):
        string_hash = self._hash(_string)
        if self.hash_table[string_hash]:
            for i, _str in enumerate(self.hash_table[string_hash]):
                if _str == _string:
                    break
            else:
                return
            self.hash_table[string_hash].remove(_str)

    def find_string(self, _string):
        string_hash = self._hash(_string)
        for _str in self.hash_table[string_hash]:
                if _str == _string:
                    print("yes")
                    break
        else:
            print("no")

    def _hash(self, _string):
        result_hash = 0
        for i, _chr in enumerate(_string):
            result_hash += (ord(_chr) * self.x_pow[i]) % self.p
        
        return result_hash % self.p  % self.size

    def check_i(self, i):
        print(" ".join(self.hash_table[int(i)]))

    def handle(self, _input):
        cmd, arg = _input.split()
        self.handler_dict[cmd](arg)


if __name__ == "__main__":
    m = int(input())  # hash-table size
    n = int(input())  # request amount
    # m = 5
    # n = 12
    hash_table = ChainHash(m)
    cmds = ["add test", "add test", "find test", "del test", "find test", "find Test", "add Test", "find Test"]
    # cmds = ["add world", "add HellO", "check 4", "find World", "find world", "del world", "check 4", "del HellO", "add luck", "add GooD", "check 2", "del good"]
    for _ in range(n):
        hash_table.handle(input())
    # for cmd in cmds:
        # hash_table.handle(cmd)
