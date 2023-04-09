from typing import List


def two_sum_ii(numbers: List[int], target: int) -> List[int]:
    l, r = 0, len(numbers) - 1
    while l < r:
        if numbers[l] + numbers[r] == target:
            return l + 1, r + 1
        if numbers[l] + numbers[r] > target:
            r -= 1
        else:
            l += 1

