from typing import List


def search_insert(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            # search right
            left = mid + 1
        else:
            # search left
            right = mid - 1
    return left

