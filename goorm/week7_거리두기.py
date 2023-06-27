"""
input
1
output
5

input
2
output
17

input
3
output
63
"""

N = int(input())
dp = [[0 for _ in range(5)] for _ in range(N + 1)]
dp[0][0] = 1
MOD = 100000007
    
for i in range(1, N + 1):
    dp[i][0] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][3] + dp[i - 1][4]) % MOD
    dp[i][1] = (dp[i - 1][0] + dp[i - 1][2] + dp[i - 1][3]) % MOD
    dp[i][2] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][3] + dp[i - 1][4]) % MOD
    dp[i][3] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]) % MOD
    dp[i][4] = (dp[i - 1][0] + dp[i - 1][2]) % MOD

print(sum(dp[N]) % MOD)



# 조건에 따라 스티커를 붙일 수 있는 경우의 수 구하기 , DP 사용
# 저장해둔 값들이 어떻게 점화식으로 연결되는지를 잘 생각해보는 것이 도움이 많이 될 것.

# 저장한 값들을 활용해서 문제를 해결할 수 있을지를 그림을 그려보면서 구해보는 것이 이해에 좋다.
