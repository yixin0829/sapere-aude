# dp practice: Identify longest palindrome within strings. For example, ‘abcdedc’ has the palindrome ‘cdedc’
from time import time
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
    

###############################################
import numpy as np
# dynamic programming: O(n^2) time and O(n^2) table space
def dp(s: str) -> str:
    n = len(s)
    # tabulation bottom-up method first create a table (harder than memorization approach but faster)
    # p[i, j] = True if s[i: j+1] is a sub-palindrome
    p = np.zeros((n, n), dtype=int)

    # dynamic programming
    # * important to figure out the correct order when populate the table
    for j in range(n):
        for i in range(j, -1, -1):
            if i == j: # base case
                p[i, j] = True
            elif j == (i + 1) and (i + 1) < n: # base case
                p[i, i+1] = s[i] == s[i+1]
            else: # state transition
                p[i, j] = p[i+1, j-1] and s[i] == s[j]

            # update the longest palin (slower)
            # if p[i, j] and (j-i+1) > len(longest_palin):
            #     longest_palin = s[i: j+1]

     # get the longest palin directly faster (search the largest idx difference in the table)
    found = False
    for col in range(n, -1, -1):
        row = 0
        while row < n and col < n:
            if p[row, col]:
                longest_palin = s[row: col+1]
                found = True
                break
            row += 1
            col += 1
            
        if found: break

    # print('dp table:\n', p)
    return longest_palin

###############################################
#  dp memorization approach (top-down recursive): slower than tabulation
def dp_2(s: str) -> str:
    # p = np.zeros((n, n), dtype=int)
    pass

def p_helper(i, j, p, s) -> int:
    # base + recursion
    # if i == j:
    #     p[i, i] = True
    
    # if (i+1) == j and (i+1) < len(s):
    #     p[i, i+1] = True
    pass
    


###############################################
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
    s2 = "plyvmcthyommabcqtmqklpfkopccabybkneifgjdqhexoezlykccgpfidcqizmotounzpslphlpwghbubwthhpivqvwmvuirfhfnkjzpxyccwnuqodbdmsxybztgzvtonheaxcrpukdpgapfczulexugxghuzuvwqvgckpsgjqyzywlxtzmkqmzgavdmchnyaqzidzjfbizxgikjbsmhyikjvgveeifntxpmpgaoqbzwxyfsnexidvxdxxzzzykphrzprlzoyqqlbxbbgmyzplgqnzphbbdxitexvvjzhtpgkfpfazqiqeyczhkkooykaotkqwuuehbgfyznwjqutbltsamcmzyhzrdvvdrzhyzmcmastlbtuqjwnzyfgbheuuwqktoakyookkhzcyeqiqzafpfkgpthzjvvxetixdbbhpznqglpzymgbbxblqqyozlrpzrhpkyzzzxxdxvdixensfyxwzbqoagpmpxtnfieevgvjkiyhmsbjkigxzibfjzdizqaynhcmdvagzmqkmztxlwyzyqjgspkcgvqwvuzuhgxguxeluzcfpagpdkuprcxaehnotvzgtzbyxsmdbdoqunwccyxpzjknfhfriuvmwvqviphhtwbubhgwplhplspznuotomziqcdifpgcckylzeoxehqdjgfienkbybaccpokfplkqmtqcbammoyhtcmvylp"
    print(bf(s))
    print(sol_expand(s))
    
    start = time()
    print(dp(s2))
    end = time()
    print(f'dp time: {end - start:.4f}')

if __name__ == '__main__':
    main()
