from typing import List


def missing_number(nums: List[int]) -> int:
    actual_sum = sum(nums)
    n = len(nums)
    expected_sum = (n * (n + 1)) // 2
    return expected_sum - actual_sum


def missing_number_alternate(nums: List[int]) -> int:
    xor_sum = 0
    for i, n in enumerate(nums):
        xor_sum ^= (i+1) ^ n
    return xor_sum
