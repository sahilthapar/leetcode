def max_product_subarray(nums: list) -> int:
    res = max(nums)
    cur_min, cur_max = 1, 1

    for n in nums:
        tmp = n * cur_max
        cur_max = max(n * cur_min, tmp, n)
        cur_min = min(n * cur_min, tmp, n)
        res = max(cur_max, res)
    return res


assert max_product_subarray([2, 3, -2, 4]) == 6
assert max_product_subarray([-2, 0, -1]) == 0


