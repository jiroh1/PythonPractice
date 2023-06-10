"""
exm1
input
7
3 1 1 7 4 9 3

output 
5
"""
# 답안
import sys
input = sys.stdin.readline

N = int(input())
P = [0] + list(map(int, input().split())) + [0]
dp = [10**18 for _ in range(N + 2)]
dp[0] = 0

for i in range(N + 2):
    for k in range(1, 4):
        if i - k < 0:
            continue
        dp[i] = min(dp[i], dp[i - k])
    dp[i] += P[i]

print(dp[N + 1])