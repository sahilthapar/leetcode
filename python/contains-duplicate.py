from typing import List


def solve_using_set_length(nums: List[int]) -> bool:
    return len(nums) != set(nums)


def solve_using_hash_map(nums: List[int]) -> bool:
    hash_map = set()
    for n in nums:
        if n in hash_map:
            return True
        hash_map.add(n)
    return False




