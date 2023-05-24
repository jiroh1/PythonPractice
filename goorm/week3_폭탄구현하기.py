"""
예시1 
입력
3 3
3 3
3 3
1 1

출력
9

예시2
입력
4 4
1 1
4 4
3 3
2 4

출력
15
"""

# 제출 답안
import sys

input = sys.stdin.readline

N, K = map(int,input().split())
bomb_list=[[0 for _ in range(N+1)] for _ in range(N+1)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for _ in range(K):
	y,x = map(int,input().split())
	bomb_list[y][x] += 1
	for i in range(4):
		ny, nx = y + dy[i] , x + dx[i]
		if ny < 0 or nx < 0  or ny > N or nx > N :
			continue
		bomb_list[ny][nx] +=1 

ans = 0
for i in range(1, N+1):
	for j in range(1, N+1):
		ans += bomb_list[i][j]

print(ans)




# 단순계산으로 해결하는 방법
import sys

input = sys.stdin.readline

N, K = map(int,input().split())


ans = 0
for _ in range(K):
    y, x = map(int, input().split())
    ans += 5 - (y == 1) - (y == N) - (x == 1) - (x == N)
print(ans)
