def min_rotated_array(nums: list[int]) -> int:
    """
    Search a rotated array with all unique elements for the minimum using recursive binary search
    :param nums:
    :return:
    """

    # set a left and right pointer
    l, r = 0, len(nums) - 1

    # if list is already sorted return the first element
    if l == r or nums[l] < nums[r]:
        return nums[l]

    # find the middle index
    m = (l+r) // 2

    # if the middle number is greater than the left pointer
    # it means that the left side is already sorted so search only the right side
    if nums[m] >= nums[l]:
        return min(nums[m], min_rotated_array(nums[m+1:]))

    # otherwise the right side has the smallest number
    return min(nums[m], min_rotated_array(nums[:m]))

# x = min_rotated_array([2, 3, 1])
# print(x)
