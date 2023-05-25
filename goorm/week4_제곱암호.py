"""
exm1

input
8
a1b2c3e4

output
bflu

exm2
input
6
z2y2z1

output
dca

"""


# N = int(input())
# S = list(input().rstrip())

# a_list=[a for a in S[::2]]
# n_list=[int(n) for n in S[1::2]]

# ans=[]

# for i in range(N//2):
# 	plus=ord(a_list[i]) + n_list[i]**2
# 	if plus <= 122:
# 		ans.append(chr(plus))
# 	elif plus >122:
# 		ans.append(chr(plus-122+96))
# print(''.join(ans))


import sys
input = sys.stdin.readline

N = int(input())
S = list(input().rstrip())
res = ''

for i in range(0, N, 2):
    c = S[i]
    n = int(S[i + 1])
    d = chr((ord(c) - ord('a') + n * n) % 26 + ord('a'))
    res += d

print(res)