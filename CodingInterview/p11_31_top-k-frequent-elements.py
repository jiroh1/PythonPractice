'''
347. Top K Frequent Elements
Medium

Share
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]


Constraints:
1 <= nums.length <= 105
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
'''

import collections

nums = [1,1,1,2,2,3]
k = 2
ans=[]
for i in nums:
    a = collections.Counter(nums)

for j in a:
    print(j,'**')
    print(a[j],'***')
    if a[j] >=k :
        ans.append(j)
print(ans)

b= list(zip(*collections.Counter(nums).most_common(k)))[0]
#print(b,'8')
#print(a[2])
print(a)