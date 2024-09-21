from typing import List

def solution(numbers: List[int]) -> List[List[int]]:
    # If empty list then return the list
    n = len(numbers)
    if n == 0:
        return []
    # set up a result list
    # set up a tracker for the starting positions
    result = []
    cur = 0
    # sort the numbers
    numbers.sort()
    for i in range(1, n):
        # if non-contiguous, end tracking, add to result
        # also update cur to starting tracking again
        if numbers[i] - numbers[i-1] > 1:
            result.append([numbers[cur], numbers[i-1]])
            cur = i
    # add the last resultant set
    result.append([numbers[cur], numbers[n-1]])
    return result



assert solution([1,2,3,4,5,40,41,42,50]) == [[1,5], [40,42],[50,50]]
assert solution([1,3,4,5,40,41,42,50]) == [[1,1], [3, 5], [40,42],[50,50]]
assert solution([40, 41, 41, 42, 1, 2, 50, 3, 4]) == [[1,4], [40,42], [50,50]]
assert solution([]) == []
assert solution([1]) == [[1, 1]]