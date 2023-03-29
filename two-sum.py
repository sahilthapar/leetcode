def two_sum(numbers: list, total: int):
    """
    This method checks if any two numbers in a list of positive unique integers
    add up to a provided sum
    :param numbers: list of positive unique integers
    :param total: desired sum
    :return: indices of the two numbers that add up to the required sum if found else -1
    """
    hash_map = dict()
    for i, n in enumerate(numbers):
        diff = total - n
        if diff in hash_map:
            return [hash_map.get(diff), n]
        hash_map[n] = i
    return -1


# print(two_sum([1, 2, 3, 4], 3))
