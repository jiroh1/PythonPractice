'''
21. Merge Two Sorted Lists - https://leetcode.com/problems/merge-two-sorted-lists/

Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

Example 1:
Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: l1 = [], l2 = []
Output: []

Example 3:
Input: l1 = [], l2 = [0]
Output: [0]

'''
# l1.val = 1 , l1.next.val = 2, l1.next.next.val=4
l1 = [1,2,4]
l2 = [1,3,4]
# 실제로는 노드의 첫머리 만 주는 것이고, 이건 리스트 값을 주는 것
a = l1+l2
print(a)
for i in l2 :
    l1.append(i)
l1=sorted(l1)
print(l1)