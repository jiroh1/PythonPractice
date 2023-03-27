'''
20. valid parentheses
https://leetcode.com/problems/valid-parentheses/
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.


Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

'''
def isValid(self, s:str) -> bool:
    stack = []
    table = {
        ')':'(',
        '}':'{',
        ']':'['
    }
    for char in s:
        if char not in table:
            stack.append(char)
        elif not stack or table[char] != stack.pop():
            return False
    return len(stack)==0

if __name__ == '__main__':
    s="()"
    print(isValid(s))



