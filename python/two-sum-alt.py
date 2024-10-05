# Alternate solution for a two sum problem

# solve it like a 3 sum problem
# sort the array, O(nlogn)
# and then use two pointers

def twoSum(nums, target):
    if len(nums) < 2:
        return []
    nums = sorted(nums)
    left, right = 0, len(nums)-1

    # if the current sum < target, need more so move left towards right
    # if the current sum > target, need less so move right towards left
    # keep going until they don't match
    # exit if solution is found

    while left < right:
        cur_sum = nums[left] + nums[right]
        if cur_sum == target:
            return [nums[left], nums[right]]
        if cur_sum < target:
            left += 1
        else:
            right -= 1


def test_empty_array():
    nums = []
    target = 0
    assert twoSum(nums, target) == []

def test_single_element():
    nums = [2]
    target = 3
    assert twoSum(nums, target) == []

def test_two_elements_sum():
    nums = [2, 7]
    target = 9
    assert twoSum(nums, target) == [2, 7]

def test_multiple_solutions():
    nums = [3, 2, 4]
    target = 6
    assert twoSum(nums, target) in ([2, 4], [4, 2])

def test_no_solution():
    nums = [3, 3]
    target = 6
    assert twoSum(nums, target) == [3, 3]

if __name__ == '__main__':
    test_empty_array()
    test_single_element()
    test_two_elements_sum()
    test_multiple_solutions()
    test_no_solution()
