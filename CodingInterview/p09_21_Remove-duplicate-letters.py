'''

'''
a="bcabc"
a=sorted(a)
print(a)

s="bcabc"
for char in sorted(set(s)):
    lis= s[s.index(char):]
    if set(s) == set(lis):
        a= char + s(lis.replace(char,''))
        print(a)
print('')

'''
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        for char in sorted(set(s)):
            lis= s[s.index(char):]
            if set(s) == set(lis):
                return char + self.removeDuplicateLetters(lis.replace(char,''))
        return ''
'''