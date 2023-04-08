from typing import List


def house_robbers(nums: List[int]) -> int:
    house1, house2 = 0, 0

    for n in nums:
        house1, house2 = house2, max(n + house1, house2)
    return house2
