from typing import List


def counting_bits(n: int) -> List[int]:
    offset = 1
    res = [0] * (n + 1)
    for i in range(1, n+1):
        if i == offset * 2:
            offset *= 2
        res[i] = 1 + res[i - offset]
    return res
