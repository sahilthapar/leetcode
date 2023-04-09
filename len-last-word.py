def len_of_last_word(s: str) -> int:
    return len(s.split()[-1])


def len_of_last_word_two(s: str) -> int:
    i, n = len(s) - 1, 0

    while s[i] == ' ':
        i -= 1
    while i >= 0 and s[i] != ' ':
        n += 1
        i -= 1
    return n
