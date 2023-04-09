def is_happy(n: int) -> bool:
    def sum_of_digit_squares(x: int) -> int:
        total = 0
        while x:
            total += (x % 10) ** 2
            x = x // 10
        return total
    nums_seen = set()
    while n not in nums_seen:
        nums_seen.add(n)
        n = sum_of_digit_squares(n)
        if n == 1:
            return True
    return False

