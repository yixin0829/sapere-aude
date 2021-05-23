# dp practice: Identify longest palindrome within strings. For example, ‘abcdedc’ has the palindrome ‘cdedc’

from typing import List

# brute force: time O(n^3) there're (n choose 2) binomial substr and takes O(n) to verify each
def bf(s: str) -> str:
    n = len(s)
    longest_palin = ''
    for i in range(n):
        for j in range(n):
            # get the substr (note '+1' is important)
            ss = s[i:j+1]
            if ispalin(ss) and len(longest_palin) < len(ss):
                longest_palin = ss

    return longest_palin

def ispalin(s: str) -> bool:
    l = 0
    r = len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1

    return True
    

import numpy as np
# dynamic programming: O(n^2) time and O(n^2) table space
def dp(s: str) -> str:
    # tabulation method first create a table
    n = len(s)
    p = np.zeros((n, n), dtype=bool)
    longest_palin = ''

    # init base case
    for i in range(n):
        p[i, i] = True
        if (i + 1) < n:
            p[i, i+1] = s[i] == s[i+1]

    # dynamic programming
    # bug: need to figure out the order when populate the table
    for i in range(n):
        for j in range(n):
            if i > j or i:
                continue
            p[i, j] = p[i+1, j-1] and s[i] == s[j]
            if p[i, j] and (j-i+1) > len(longest_palin):
                longest_palin = s[i: j+1]

    print(p)
    return longest_palin

# expansion method: O(n^2) time and O(1) space
def sol_expand(s: str) -> str:
    # expand at every mid points and update the longest sub-palindrome
    # note we will have to expand (2n -1) times since mid pt could be in b/w (e.g 'abba')
    longest_palin = ''
    for i in range(len(s)):
        # check odd palindrome
        l = i - 1
        r = i + 1
        while l >= 0 and r < len(s):
            if s[l] != s[r]:
                break
            l -= 1
            r += 1

        sub = s[l+1: r] # note r is not included so we don't -1
        if len(sub) > len(longest_palin):
            longest_palin = sub

        # check even palindrome
        l = i
        r = i + 1
        while l >= 0 and r < len(s):
            if s[l] != s[r]:
                break
            l -= 1
            r += 1

        sub = s[l+1: r] # note r is not included so we don't -1
        if len(sub) > len(longest_palin):
            longest_palin = sub

    return longest_palin

def main():
    s = 'abcdefedc'
    print(bf(s))
    print(sol_expand(s))
    print(dp(s))

if __name__ == '__main__':
    main()
