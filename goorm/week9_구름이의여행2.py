
"""
exm1
input
5 6 4
1 2
1 4
3 1
4 2
4 5
5 3
output
4

exm2
input
5 6 4
1 2
1 3
3 2
4 2
5 1
5 4
output
-1
"""

from collections import deque
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
G = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    
D = [9**9 for _ in range(N + 1)]
D[K] = 0
Q = deque()
Q.append(K)
ans = 9**9

while Q:
    cur = Q.popleft()
    for next in G[cur]:
        # n_p에 해당하는 정점을 찾았을 때 답을 갱신합니다.
        if next == K:
            ans = min(ans, D[cur] + 1)
        if D[next] <= D[cur] + 1:
            continue
        D[next] = D[cur] + 1
        Q.append(next)
        
if ans == 9**9:
    print(-1)
else:
    print(ans)
