'''
6
z2a1y5
'''

# 첫 제출 답안인데 제출 후 답이 틀린 경우가 많았다.
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


# 최종답안
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
--------
내가 찾은 반례

4
a9z9


반례 1
입력
4
z4a2
정답 : pe
출력 : Ve

반례 2
6
z2a1y5
정답 : dbx
출력 : db^

"""