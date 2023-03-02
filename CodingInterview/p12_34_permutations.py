'''
46. Permutations
Medium

Share
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]
'''
import itertools

nums = [1,2,3]
ans = []


an = list(itertools.permutations(nums))
bn = list(map(list,itertools.permutations(nums)))
print(an)
print(bn)