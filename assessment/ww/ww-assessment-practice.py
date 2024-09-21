from typing import List

# def is_palindrome(s):
#     return s == s[::-1]
#
#
# def solution(s):
#     for i in range(len(s)-1, -1, -1):
#         if is_palindrome(s[:i+1]) and len(s[:i+1]) >= 2:
#             return solution(s[i+1:])
#     return s
#
# assert solution("aaacodedoc") == ''
# assert solution("codesignal") == 'codesignal'
# assert solution("") == ''

# def solution(a, k):
#     l = 0
#     r = sum(a) // k
#     while l <= r:
#         m = (l + r) // 2
#         if can_cut(a, k, m):
#             l = m + 1
#         else:
#             r = m - 1
#     return r
#
#
# def can_cut(a, k, length):
#     return sum([i // length for i in a]) >= k
#
# assert solution([5, 2, 7, 4, 9], 5) == 4
# assert solution([1, 2, 3, 4, 9], 6) == 2
# assert solution([4, 8, 4, 5, 3, 7, 1, 2, 6], 5) == 4