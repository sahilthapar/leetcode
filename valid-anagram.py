import collections

def valid_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    cnt_s, cnt_t = {}, {}

    for i in range(len(s)):
        cnt_s[s[i]] = 1 + cnt_s.get(i, 0)
        cnt_t[t[i]] = 1 + cnt_t.get(i, 0)

    for c in cnt_s:
        if cnt_s[c] != cnt_t.get(c, 0):
            return False
    return True


def valid_anagram_two(s: str, t: str) -> bool:
    return collections.Counter(s) == collections.Counter(t)


def valid_anagram_three(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)