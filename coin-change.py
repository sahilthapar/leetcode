from typing import List


def coin_change(coins: List[int], amount: int) -> int:
    solution = [amount + 1] * (amount + 1)
    solution[0] = 0

    for a in range(1, amount+1):
        for c in coins:
            if a - c >= 0:
                solution[a] = min(solution[a], 1 + solution[a-c])

    return solution[amount] if solution[amount] != [amount + 1] else - 1
