from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """
        This method checks if any two numbers in a list of positive unique integers
        add up to a provided sum
        :param nums: list of positive unique integers
        :param target: desired sum
        :return: indices of the two numbers that add up to the required sum if found else -1
    """
    hash_map = dict()
    for i, n in enumerate(nums):
        diff = target - n
        if diff in hash_map:
            return [hash_map.get(diff), i]
        hash_map[n] = i
    return -1