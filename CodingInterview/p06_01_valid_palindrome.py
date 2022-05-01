'''
125. Valid Palindrome
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

isalnum() - https://it-neicebee.tistory.com/43
'''
exm="race a car"
exm=list(exm)
res=[]
for alp in exm:
    if alp.isalpha():
        res.append(alp.lower())
# print(res)
# print(res.pop(3),res.pop(4))
while len(res)>1:
    if res.pop(0) != res.pop():
        print("1")
print("end")

'''
answer - 
class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = []
        for alp in s:
            if alp.isalpha():
                res.append(alp.lower())
        while len(res)>1:
            if res.pop(0) != res.pop():
                return False

        return True

'''