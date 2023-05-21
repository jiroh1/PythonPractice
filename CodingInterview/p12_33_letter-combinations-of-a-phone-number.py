'''
17. Letter Combinations of a Phone Number
Medium

Share
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]

Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
'''
'''
dic = {"2": "abc","3": "def", "4":"ghi", "5":"jkl", "6":"mno","7":"pqrs", "8":"tuv", "9":"wxyz"}
digits="23"
res = []
#입력번호 범위
for i in range(index, len(digits)):
    for j in dic[digits[i]]:
        if len(path) == len(digits):
            res.append(path)
            return res
'''
class Solution:
    def letterCombinations(self, digits: str) :
        dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        result = []

        def dfs(index, path):
            #끝까지 탐색해서 백트레킹
            if len(path) == len(digits):
                result.append(path)
                return

            #입력값 자릿수 단위 반복
            for i in range(index, len(digits)):
            #숫자에 해당하는 모든 문자열 반복
                for j in dic[digits[i]]:
                    dfs(i + 1, path + j)

        #예외 처리
        if not digits:
            return []


        dfs(0, "")

        print(dfs())

if __name__ == '__main__':
    digits="23"



'''


i : 0, j: a, dfs(1, a)
i : 1, j: d, dfs(2, ad)
['ad']
return

i : 1, j: e, dfs(2, ae)
['ad', 'ae']
return

i : 1, j: f, dfs(2, af)
['ad', 'ae', 'af']
return

i : 0, j: b, dfs(1, b)
i : 1, j: d, dfs(2, bd)
['ad', 'ae', 'af', 'bd']
return

i : 1, j: e, dfs(2, be)
['ad', 'ae', 'af', 'bd', 'be']
return

i : 1, j: f, dfs(2, bf)
['ad', 'ae', 'af', 'bd', 'be', 'bf']
return

i : 0, j: c, dfs(1, c)
i : 1, j: d, dfs(2, cd)
['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd']
return

i : 1, j: e, dfs(2, ce)
['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce']
return

i : 1, j: f, dfs(2, cf)
['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
return

i : 1, j: d, dfs(2, d)
i : 1, j: e, dfs(2, e)
i : 1, j: f, dfs(2, f)

'''

