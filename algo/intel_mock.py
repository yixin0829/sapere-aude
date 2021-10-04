#
##################### Intel Mock 1 (60 min) ########################

import unittest
from typing import List
from time import time, sleep

from bisect import bisect, bisect_left, bisect_right
from collections import deque, Counter

import numpy as np
import pandas as pd

# Q1
# Function Given a node return a node (endpoint - last node in the path) -
 
#  PROPERTY: Every node on the path has only 1 input and 1 output, with the exception of the start node (which can have any number of inputs)
#            and the end node (which can have any number of outputs)
# input: node* (error checking property)
# output: node* (endpoint in the longest path)
# Examples: 
#    E
#    ^
#    |
# A->B->C
#    ^
#    |
#    D

class Node:
    def __init__(self, input_, output_):
        input_ = input
        output_ = output
        

# def find_node(n: Node) -> Node:
#     # check if the node is an endpoint
#     if len(n.output_) > 1:
#         return n

#     # if not an endpoint
#     end_pt = False
#     while n is not end point:
#         n = n.next
#         check if n is end pt and set the flag
    
#     return n

def find_node(n: Node) -> Node:
    # check if the node is an endpoint
    if len(n.output) > 1 or len(n.output) == 0:
        return n # return the endpoint

    # not an endpoint
    end_pt = False
    n = n.output[0]
    while len(n.output) == 1:
        n = n.output[0]

    return n

# Q2
# Count the number of sets of anagrams in input[]
#    For example:
#      input1[] = { "act", "toe", "cat", "opt", "pot" }
#        returns 2 { "act", "cat" } { "opt", "pot" }
#      input2[] = { "bee", "red", "ebb", "bed" }
#        returns 0
#      input3[] = { "top", "pot", "opt", "wee", "ewe", "and", "dan" }
#        returns 3 { "top", "pot", "opt" } { "wee", "ewe" } { "and", "dan" }

# n strings in input
# each string has fixed length O(1)
# takes O(1) time to construct a "finger print" (counter, more specifically a dict)
# time: O(N) and space: O(N)

def helper(s: str) -> tuple:
    counter = [0] * 26 
    for c in s:
        counter[ord(c) - ord('a')] += 1 

    return tuple(counter)
    

# O(2N) ~= O(N) time
def count_anagram_sets(input: List[str]) -> int:
    d = {}

    for word in input: # O(N) time
        counter = helper(word)
        if counter in d:
            d[counter] += 1
        else:
            d[counter] = 1

    ans = 0
    for key in d.keys(): # O(N) time worst case
        if d[key] > 1:
            ans += 1
    
    return ans

def anagram_sets(input: List[str]) -> int:
    d = {}

    for word in input: # O(N) time
        counter = helper(word)
        if counter in d:
            d[counter].append(word)
        else:
            d[counter] = [word]

    ans = []
    for key in d.keys(): # O(N) time worst case
        if len(d[key]) > 1:
            ans.append(d[key])
    
    return ans
keywords = ["hi", "hello", "bye", "helol", "abc", "cab", 
                "bac", "silenced", "licensed", "declines"]

print(count_anagram_sets(keywords))
print(anagram_sets(keywords))
print('hello'' world')


# Q3
# [2, 4, 7, 1, 4, -5, 6, 10, 0, 3] t=12 ("two sum")
# return True/False whether there exists any pair sum equal to the target

# one-pass approach
# def two_sum(nums: List[int], target: int) -> bool:
#     for number in nums:
#         calculate the complement of the target (say cp)
#         find cp in dict

#         if not found
#             put number in dict
#         else:
#             return True


# time: O(N)
def two_sum(nums: List[int], target: int) -> bool:
    d = {}
    for num in nums: # O(N)
        cp = target - num
        if cp not in d: # O(1)
            d[num] = 1
        else: # found the complment of target (seen it before)
            return True

    return False
