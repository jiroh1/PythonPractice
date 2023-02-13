'''
234. Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/

Given the head of a singly linked list, return true if it is a palindrome.

Example 1:
Input: head = [1,2,2,1]
Output: true
Example 2:
Input: head = [1,2]
Output: false

#발생했던 에러
AttributeError: 'list' object has no attribute 'next'
사이트 상에서 나온 에러
TypeError: 'ListNode' object is not iterable for i in head
'''

head = [1,2,2,1]
check=[]
# print(head.next)
for i in head:
    check.append(i)
print(check)
#
# while head is not None:
#     check.append(head.val)
#     head=head.next
#     print(head)

while len(head)>1:
    if head.pop(0) !=head.pop():
        print(False)
print(True)
'''
if (not l1) or (l2 and l1.val > l2.val):
    l1, l2 = l2, l1
if l1:
    l1.next = self.mergetTwoLists(l1.next, l2)
return l1

'''
'''
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        q:List =[]
        if not head:
            return True
        node=head
        
        #리스트 변환
        while node is not None:
            q.append(node.val)
            node=node.next
            
        #펠린드롬 판별
        while len(q)>1:
            if q.pop(0) != q.pop():
                return False
        return True
'''