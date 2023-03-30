def search(nums: list, target: int) -> int:
    return modified_binary_search(nums, target, left=0, right=len(nums) - 1)


def modified_binary_search(nums: list, target: int, left: int, right: int) -> int:
    middle = (left + right) // 2
    if nums[middle] == target:
        return middle
    if left == right:
        return - 1
    if nums[left] <= nums[middle]:
        if target > nums[middle] or target < nums[left]:
            left = middle + 1
        else:
            right = middle - 1
    else:
        if target < nums[middle] or target > nums[right]:
            right = middle - 1
        else:
            left = middle + 1
    return modified_binary_search(nums, target, left, right)


assert search(nums=[4, 5, 6, 7, 0, 1, 2], target=0) == 4
assert search(nums=[4, 5, 6, 7, 0, 1, 2], target=3) == -1
assert search(nums=[2], target=0) == -1
