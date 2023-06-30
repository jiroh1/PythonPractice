



"""
예시1
입력
6
4 1
2 1
6 2
3 6
4 5
3 2
출력
3
2 3 6

예시2
입력
6
2 5
4 6
3 5
3 1
2 3
5 6
출력
3
2 3 5

"""

import sys
input = sys.stdin.readline

N = int(input())
G = [[] for _ in range(N + 1)]
V = [0 for _ in range(N + 1)]
for _ in range(N):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

# 현재 방문한 정점을 기록하는 스택입니다.
ST = []
# 사이클의 시작점을 의미하는 변수입니다.
start = -1

def DFS(cur, prev):
    global start
    ST.append(cur)
    for next in G[cur]:
        if start != -1:
            return
        # 바로 직전 정점과는 사이클을 이룰 수 없으므로, 예외처리를 해줘야 합니다.
        if next == prev:
            continue
        # 다음 정점이 이미 방문한 정점인 경우, 해당 정점을 사이클의 시작점으로 설정하고 DFS를 탈출합니다.
        if V[next]:
            start = next
            return
        V[next] = 1
        DFS(next, cur)
    # 사이클의 시작 정점을 찾은 경우, 방문한 정점 목록을 보존해야 하므로 DFS를 더 수행하면 안 됩니다.
    if start != -1:
        return
    ST.pop()

V[1] = 1
DFS(1, 0)

# 현재 스택에는 사이클을 이루는 경로가 역순으로 저장되어 있습니다.
# 사이클의 시작 정점이 보일 때까지 스택에서 원소들을 뽑아줍니다.
ans = []
while 1:
    ans.append(ST[-1])
    ST.pop()
    if ans[-1] == start:
        break
    
ans.sort()
print(len(ans))
print(*ans)