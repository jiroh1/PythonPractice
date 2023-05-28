# 뿌요 쌍을 스택에 들어오기 전에 기존 뿌요 쌍을 터트릴지 말지 를 결정해줘야 함

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = input().rstrip()
Q = []
Q.append(('', 1)) # index error를 피하기 위해서 넣음 , 이것을 생각하는 것이 제일 어렵다고 생각함

S += 'z'
for c in S:
    if Q[-1][0] != c:
        if M <= Q[-1][1]: # M 보다 크거나 같은 숫자이면 터져야 하기 때문에 
            top = Q[-1][0] # 같은 것을 계속 넣었으니 top으로 정하고
            while top == Q[-1][0]: # 그 정한 top과 같은 것들을 계속 뺀다.
                Q.pop()
    if Q[-1][0] == c: # 같은 문자면 [1] 에 +1을 더해서 같은 것의 갯수를 작성해준다.
        Q.append((c, Q[-1][1] + 1))
    else: # 같지 않은 문제들이면 새로 추가 해주는 것 
        Q.append((c, 1))
Q.pop() # ('z',1) 이것도 없애주는 것. 위에 index error 피하기 위해 하는 것만큼 어려운듯.

if len(Q) > 1:
    for c, n in Q:
        print(c, end='')
else:
    print("CLEAR!")




"""
exm 1
input
9 2
ABCCBCCDA

output
ADA

exm2
input
10 3
ABCCCBBAAA

output
CLEAR!
"""