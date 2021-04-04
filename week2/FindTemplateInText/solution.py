import random
from time import time

def _hash(substring, x, p, pow_x):
    hash_result = 0
    i = 0
    for char in substring:
        hash_result += ord(char) * pow_x[i] % p 
        i += 1
    return hash_result % p


def get_sub_hashes(text, last_hash, p, last_member, pattern_len, x):
    result = [last_hash]
    prev_hash = last_hash
    for i in range(len(text)-pattern_len-1, -1, -1):
        h = (((prev_hash % p - (ord(text[i + pattern_len]) * last_member % p) % p) % p + p % p) * (x % p)) % p + \
            ord(text[i]) % p
        prev_hash = h
        result.append(h)
    return result[::-1]


def get_mathces(pattern, text):
    """Karp-Rabin's Algorithm"""
    p = 1000000007  # big simple digit
    pattern_len = len(pattern)
    # x = random.randint(1, p)
    x = 1
    result = []
    last_member = pow(x, (pattern_len - 1))
    llen = pattern_len if pattern_len > len(text[-pattern_len: ]) else len(text[-pattern_len: ])
    pow_x = [pow(x, i) for i in range(llen)]
    last_hash = _hash(text[-pattern_len: ], x, p, pow_x)
    pattern_hash = _hash(pattern, x, p, pow_x)
    sub_hashes = get_sub_hashes(
        text, last_hash, p, last_member, pattern_len, x)

    i = 0
    for _hash1 in sub_hashes:
        if _hash1 == pattern_hash:
            if pattern == text[i: i + pattern_len]:
                result.append(i)
        i += 1

    return result


if __name__ == "__main__":
    # pattern = input()
    # text = input()
    t = time()
    pattern = "aba"
    text = "abacaba"

    print("result: {0}".format(get_mathces(pattern, text)))
