"""
안전지대
https://school.programmers.co.kr/learn/courses/30/lessons/120866
"""
# 제출 답안
def solution(board):
    answer = 0
    max_r, max_c = len(board),len(board[0])
    for idx_r in range(max_r):
        for idx_c in range(max_c):
            dirs = ((-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1))
            # 나 자신이 안전한 경우
            if board[idx_r][idx_c] == 0:
                is_safe = True
                # 8 방향에 대한 체크를 진행 
                count=0
                for mov_r, mov_c in dirs:
                    count+=1
                    check_r, check_c = idx_r + mov_r, idx_c + mov_c
                    # 범위 내에 있을 경우
                    if check_r in range(max_r) and check_c in range(max_c):
                        # 안전지대가 아닌 경우
                        if board[check_r][check_c] == 1:
                            is_safe = False
                if is_safe:
                    answer += 1
    return answer


board=[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
print(solution(board))


"""
접근방식
    # [i][j]  i: 위 -1, 아래: +1 /j: 좌 -1, 우 +1 
    # 대각선 i-1 (j-1,j+1) , i+1 (j-1,j+1)
    # 그래서 한바퀴 돌면서 1이면
    # board 에 확인해서 1로 바꾸는 것 하면 됨 
    # COUNT 로 변경된 것들 을 Answer에 넣어주려고했음
    # 그러면 이제 그 외에 넘어가는 부분 없애면 됨

# 처음 대략적으로 구현했던 코드 -> 이것도 제법 정확성 61.1 까지 나왔음 (안될 줄 알았음)
def solution(board):
    answer = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                try:
                    board[i-1][j] = -1
                    board[i+1][j] = -1
                    board[i][j-1] = -1
                    board[i][j+1] = -1
                    board[i-1][j-1] = -1
                    board[i-1][j+1] = -1
                    board[i+1][j-1] = -1
                    board[i+1][j+1] = -1
                except:
                    pass
    
    for k in board:
        answer+=k.count(-1)
        answer+=k.count(1)
    return (len(board))**2 - answer

"""
"""
다른풀이
# case 1
def solution(board):
    n = len(board)
    danger = set()
    for i, row in enumerate(board):
        for j, x in enumerate(row):
            if not x:
                continue
            danger.update((i+di, j+dj) for di in [-1,0,1] for dj in [-1, 0, 1])
    return n*n - sum(0 <= i < n and 0 <= j < n for i, j in danger)

# case 2 - numpy 이용
import numpy as np
from collections import Counter

def solution(board):
    n = len(board)
    # pad() 함수를 사용해 주어진 2차원 배열의 상하좌우 1줄씩 -1을 추가한 board_padded 생성
    board_padded = np.pad(board, ((1, 1), (1, 1)), constant_values = -1)
    danger_array = np.pad(board, ((1, 1), (1, 1)), constant_values = -1)
    for i in range(1, n+1):
        for j in range(1, n+1):
            if board_padded[i][j] == 1:
                for x in range(i-1, i+2):
                    for y in range(j-1, j+2):
                        danger_array[x][y] = 1
    danger_list = danger_array.reshape(1, -1).squeeze()
    answer = Counter(danger_list)[0]
    # 결과 값 반환
    return answer


# case 3 - BFS
from collections import deque

def solution(board):
    dx = [-1, 1, 0 , 0, 1, 1, -1, -1]
    dy = [0, 0, -1, 1, -1, 1, 1, -1]
    length = len(board)
    visited = [[False] * length for _ in range(length)]

    def bfs(x, y):
        dq = deque()
        dq.append((x, y))
        while dq:
            a, b = dq.popleft()
            visited[a][b] = True
            for i in range(8):
                nx = dx[i] + a
                ny = dy[i] + b
                #위험지역으로 둬야함 
                if 0<=nx<length and 0<=ny<length and not visited[nx][ny]:
                    if board[nx][ny] == 1:
                        dq.append((nx, ny))
                    else:
                        board[nx][ny] = 2 #위험지역 처리 

    for i in range(length):
        for j in range(length):
            if board[i][j] == 1:
                bfs(i, j)
    result = 0
    for i in range(length):
        result += board[i].count(0)
    return result
"""
"""
정리
1. 처음 접근 방식으로 먼저 해당하는 부분에 모두 위험범위로 바꾸고 안전한 곳을 세려고 했는데, 중복되는 것을 정확히 다루기에는 시간이 부족했다.
2. 제출한 코드는 유튜브를 통해서 배운 것인데, 각 위치 마다 폭탄이 있는지 없는지를 확인 하는 코드이다.
3. '2'와 같은 생각으로 접근 하는 방식을 했어야 했던 것 같다.
4. 각 좌표에서 총 8개의 방향으로 1이 있으면 그것은 False로 빠지면서 answer에 추가 되지 않는 것이다.
5. numpy 사용과 BFS 가 있는데, 확실히 numpy 보다는 BFS 쓰는게 속도가 빨랐다

"""
"""
참고 사이트
https://www.youtube.com/watch?v=jJWlodLCCrs
# case 2, 3
https://velog.io/@seulki971227/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-Lv.0-%EC%95%88%EC%A0%84%EC%A7%80%EB%8C%80-Python
"""