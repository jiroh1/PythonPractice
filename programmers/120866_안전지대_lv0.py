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

# def solution(board):
#     answer = 0
#     r_max, c_max = len(board),len(board[0])
#     for r_idx in range(r_max):
#         for c_idx in range(c_max):
#             dirs = ((-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1))
#             # 나 자신이 안전한 경우
#             if board[r_idx][c_idx] == 0:
#                 is_safe = True
#                 # 8 방향에 대한 체크를 진행 
#                 for r_mov, c_mov in dirs:
#                     r_check, c_check = r_idx + r_mov, c_idx + c_mov
#                     # 범위 내에 있을 경우
#                     if r_check in range(r_max) and c_check in range(c_max):
#                         # 안전지대가 아닌 경우
#                         if board[r_check][c_check] == 1:
#                             is_safe = False
#                 if is_safe:
#                     answer += 1
#     return answer


"""
접근방식
    # [i][j]  i: 위 -1, 아래: +1 /j: 좌 -1, 우 +1 
    # 대각선 i-1 (j-1,j+1) , i+1 (j-1,j+1)
    # 그래서 한바퀴 돌면서 1이면
    # board 에 확인해서 1로 바꾸는 것 하면 됨 
    # COUNT 로 변경된 것들 을 Answer에 넣어주려고했음
    # 그러면 이제 그 외에 넘어가는 부분 없애면 됨

# 처음 대략적으로 구현했던 코드 -> 이것도 제법 정확성 61.1 까지 나왔음
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

"""
"""
정리
1. 처음 접근 방식으로 먼저 해당하는 부분에 모두 위험범위로 바꾸고 안전한 곳을 세려고 했는데, 중복되는 것을 정확히 다루기에는 시간이 부족했다.
2. 제출한 코드는 유튜브를 통해서 배운 것인데, 각 위치 마다 폭탄이 있는지 없는지를 확인 하는 코드이다.
3. '2'와 같은 생각으로 접근 하는 방식을 했어야 했던 것 같다.
4. 각 좌표에서 총 8개의 방향으로 1이 있으면 그것은 False로 빠지면서 answer에 추가 되지 않는 것이다.
"""
"""
참고 사이트
https://www.youtube.com/watch?v=jJWlodLCCrs
"""