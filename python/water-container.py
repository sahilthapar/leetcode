from typing import List


def water_container(nums: List[int]) -> int:
    left, right = 0, len(nums) - 1
    area = min(nums[left], nums[right]) * (right - left)
    while left < right:
        cur_area = min(nums[left], nums[right]) * (right - left)
        area = max(area, cur_area)
        if nums[left] < nums[right]:
            left += 1
        elif nums[left] > nums[right]:
            right -= 1
    return area


