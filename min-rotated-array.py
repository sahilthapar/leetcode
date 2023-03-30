def min_rotated_array(nums: list[int]) -> int:
    """
    Search a rotated array with all unique elements for the minimum using recursive binary search
    :param nums:
    :return:
    """
    # set a left and right pointer
    left, right = 0, len(nums) - 1

    # if list is already sorted return the first element
    if left == right or nums[left] < nums[right]:
        return nums[left]

    # find the middle index
    middle = (left + right) // 2

    # if the middle number is greater than the left pointer
    # it means that the left side is already sorted so search only the right side
    if nums[middle] >= nums[left]:
        return min(nums[middle], min_rotated_array(nums[middle + 1:]))

    # otherwise the right side has the smallest number
    return min(nums[middle], min_rotated_array(nums[:middle]))


assert min_rotated_array([3, 4, 5, 1, 2]) == 1
assert min_rotated_array([4, 5, 6, 7, 0, 1, 2]) == 0
assert min_rotated_array([11, 13, 15, 17]) == 11
