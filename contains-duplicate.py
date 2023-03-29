class ContainsDuplicate(object):
    @staticmethod
    def solve_using_set_length(nums: list) -> bool:
        return len(nums) == set(nums)

    @staticmethod
    def solve_using_hash_map(nums: list) -> bool:
        hash_map = set()
        for n in nums:
            if n in hash_map:
                return True
            hash_map.add(n)
        return False


