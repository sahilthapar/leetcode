from typing import List


def three_sum(self, nums: List[int]) -> List[List[int]]:
    # sort the array
    nums.sort()
    res = []

    for i, x in enumerate(nums):
        if i > 0 and x == nums[i-1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = x + nums[left] + nums[right]
            if total > 0:
                right -= 1
            elif total < 0:
                left += 1
            else:
                res.append([x, nums[left], nums[right]])
                left += 1
                while nums[left] == nums[left-1] and left < right:
                    left += 1
    return res