from typing import List
import heapq

def last_stone_weight(stones: List[int]) -> int:
    stones = [-i for i in stones]
    heapq.heapify(stones)

    while len(stones) > 1:
        w1 = heapq.heappop(stones)
        w2 = heapq.heappop(stones)
        if w2 > w1:
            heapq.heappush(stones, w1-w2)

    stones.append(0)
    return abs(stones[0])
