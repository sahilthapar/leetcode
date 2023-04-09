from typing import List

def remove_duplicates(nums: List[int]) -> int:
    n = len(nums)
    if n <= 1:
        return n
    k = 1
    for i in range(1, n):
        if nums[i] == nums[i - 1]:
            continue
        else:
            nums[k] = nums[i]
            k += 1
            i += 1

    return k
