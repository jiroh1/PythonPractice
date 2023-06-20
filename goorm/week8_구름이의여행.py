


"""
예시1
입력
6 6 2
1 4
4 2
2 6
4 3
1 2
3 1
출력
YES

예시2
입력
6 6 2
1 2
2 3
3 4
3 5
5 6
5 2
출력
NO


예시3
입력
3 1 1
1 2
출력
NO


"""

from collections import deque
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
G = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

D = [9**9 for _ in range(N + 1)]
D[1] = 0

Q = deque()
Q.append(1)
while Q:
    cur = Q.popleft()
    for next in G[cur]:
        if D[next] <= D[cur] + 1:
            continue
        D[next] = D[cur] + 1
        Q.append(next)
        
if D[N] <= K:
    print("YES")
else:
    print("NO")