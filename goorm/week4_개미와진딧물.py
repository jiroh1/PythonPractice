# 최종답안 1
# 최종답안 2
import sys

input=sys.stdin.readline

N, M = map(int, input().split())
ants, aphids = [], [] # ants:  [[0, 1], [1, 3], [2, 3], [3, 2]] / aphids : [[1, 1], [3, 0]]
for i in range(N):
    s = list(map(int, input().split()))
    for j in range(N):
        if s[j] == 1:
            ants.append([i, j])
        elif s[j] == 2:
            aphids.append([i, j])

ans = len(ants)
for y1, x1 in ants:
    min_dist = 9 ** 9 # 문제에서 M 에 대해서 범위를 정해줬으니 그것을 중심으로 
    for y2, x2 in aphids:
        dist = abs(y1 - y2) + abs(x1 - x2) # 맨해튼 거리를 구해보고 , 개미들이 각각의 진딧물과의 거리를 구함
        min_dist = min(min_dist, dist) # for 문을 돌면서 이미 min_dist 하나가 정해지기만 하면 (즉, 진딧물 하나만 만난다면) 큰 숫자 들은 중요하지 않으니 이렇게 정해놓음
    if min_dist > M: # y1, y2, x1, x2 : 2 1 3 1 인경우를 확인 해서 이해해야 함.
        ans -= 1

print(ans)

import sys

input=sys.stdin.readline

# M 이하에 위치한 진딧물이 수액을 채취할 수 있다.

# 땅 만들고
# 우선 그럼 개미 찾고
# 거기에서 M 이하 안에 진딧물이 있는지 없는지 확인하고
# 있으면 개미 수 추가


N, M = map(int, input().split())
earth = [list(map(int,input().split())) for _ in range(N)]

dy = [-M,M,0,0]
dx = [0,0,-M,M]

for i in range(N):
	for j in range(N):
		if earth[i][j] == 1:
			# M 이하에 2가 있는지 없는지를 확인하면 됨! 
			pass


"""
예시1
입력
4 2
2 0 0 0
2 0 0 1
2 0 0 0
2 0 0 1
출력
0

예시2
입력
4 2
0 1 0 0
0 2 0 1
0 0 0 1
2 0 1 0
출력
3

"""