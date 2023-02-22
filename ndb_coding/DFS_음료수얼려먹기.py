"""
음료수 얼려먹기
"""
# N,M을 공백으로 구분하여 입력받기
n, m = map(int,input().split())

# 2차원 리스트의 맵 정보 입력받기
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

# DFS를 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x,y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >=n or y<=-1 or y>=m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y]==0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상, 하, 좌 ,우의 위치도 모두 재귀적으로 호출
        dfs(x -1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

# 모든 노드(위치)에 대하여 음료수 채우기
result=0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1
            
print (result)



# def dfs(graph, v , visited):
#     # 현재 노드를 방문 처리
#     visited[v]=True
#     print(v,end=' ')
#     # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph,i,visited)
"""
문제
시간제한 1초 , 메모리 제한 128mb

N * M 크기의 얼음 틀이 있다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다.
구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다.
이 때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하시오.
다음의 4 * 5 얼음 틀 예시에서는 아이스크림이 총 3개 생성된다.

00110
00011
11111
00000

입력조건
- 첫번째 줄에 얼음 틀의 세로 길이 N과 가로 길이 M이 주어진다. (1<=N,M<=1000)
- 두 번째 줄부터 N+1 줄까지 얼음틀의 형태가 주어진다.
- 이 때 구멍이 뚫려있는 부분은 0, 그렇지 않은 부분은 1이다.

출력조건
- 한번에 만들 수 있는 아이스크림의 개수를 출력한다.

"""