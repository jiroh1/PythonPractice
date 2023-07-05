"""
exm1
input
3
A
BC
DEFG
output
7
11

exm2
4
K
WL
TZAL
YYWBNRJT
출력
38
83
"""

import sys
input = sys.stdin.readline

N = int(input())
S = [[] for _ in range(N + 1)]
for i in range(1, N + 1):
    S[i] = input().rstrip()
ans1, ans2 = 9**9, 0

def DFS(h, n, score):
    score += ord(S[h][n]) - ord('A') + 1
    if h < N:
        DFS(h + 1, n * 2, score)
        DFS(h + 1, n * 2 + 1, score)
    else:
        global ans1, ans2
        ans1 = min(ans1, score)
        ans2 = max(ans2, score)
    
DFS(1, 0, 0)
print(ans1, ans2, sep='\n')