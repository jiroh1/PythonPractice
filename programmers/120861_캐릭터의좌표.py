"""
캐릭터의 좌표
https://school.programmers.co.kr/learn/courses/30/lessons/120861
"""
# 제출 답안 - > 통과
def solution(keyinput, board):
    answer = [0,0]
    for key in keyinput:
        if key == "left":
            if abs(answer[0]) < abs(board[0]//2)or answer[0] > 0:
                answer[0]-=1
        elif key == "right":
            if abs(answer[0]) < abs(board[0]//2) or answer[0] < 0:
                answer[0]+=1
        elif key =='down':
            if abs(answer[1]) < abs(board[1]//2) or answer[1] > 0:
                answer[1]-=1
        elif key == 'up':
            if abs(answer[1]) < abs(board[1]//2) or answer[1] < 0:
                answer[1]+=1
    return answer



keyinput=['left','left','left','right']
board=[3,3]

print(solution(keyinput,board))
"""
정리
1. count 써서 그냥 한번에 계산 하는 것을 사용했으나 케이스 3개나 실패 (as 1st solution)
2. 그래서 key 값을 하나씩 계산해주는 것으로 해서 코딩 했으나 1개 실패( as 2nd solution)
3. 질문하기에서 테스트 케이스 확인하여 생각 해보니 아무리 left 하더라도 안하게는 이미 만들었으나, 반대로 가는 것에 대해서 생각하지 못했음
4. 그래서 각각 반대 방향에 대한 조건을 넣어주어서 해결
    testcase : keyinput=['left','left','left','right']
5. 다른 풀이 처럼 dict를 이용해서 푸는 방법을 좀 생각 하면 추후 길찾기 문제에 도움이 될것 같다.
"""
"""
다른풀이
# case 1)

def solution(keyinput, board):
    x_lim,y_lim = board[0]//2,board[1]//2
    move = {'left':(-1,0),'right':(1,0),'up':(0,1),'down':(0,-1)}
    x,y = 0,0
    for k in keyinput:
        dx,dy = move[k]
        if abs(x+dx)>x_lim or abs(y+dy)>y_lim:
            continue
        else:
            x,y = x+dx,y+dy

    return [x,y]
"""

"""
풀이 과정

# 두번째 풀이 -> 8번 실패
def solution(keyinput, board):
    answer = [0,0]
    for key in keyinput:
        if key == "left":
            if abs(answer[0]) < abs(board[0]//2):
                answer[0]-=1
        elif key == "right":
            if abs(answer[0]) < abs(board[0]//2):
                answer[0]+=1
        elif key =='down':
            if abs(answer[1]) < abs(board[1]//2):
                answer[1]-=1
        elif key == 'up':
            if abs(answer[1]) < abs(board[1]//2):
                answer[1]+=1
    return answer

# 첫번째 풀이 -> 1,7,8 실패
def solution(keyinput, board):
    left=int(keyinput.count("left"))
    right=int(keyinput.count("right"))
    up=int(keyinput.count("up"))
    down=int(keyinput.count("down"))
    row=right-left
    column=up-down
    
    # 행
    if board[0]//2 < abs(row):
        if row < 0:
            row=-board[0]//2
            print(board[0],row,board[0]//2)
        elif row > 0:
            row=board[0]//2
        
    # 열         
    if board[1]//2 < abs(column):
        if column < 0:
            column=-(board[1]//2)
        elif column > 0:
            column=board[1]//2

    answer = [ row , column]
    return answer
"""