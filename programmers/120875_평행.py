"""
평행
https://school.programmers.co.kr/learn/courses/30/lessons/120875
"""


def gradient(a,b):
    return (a[1]-b[1])/(a[0]-b[0])

def solution(dots):
    x1, y1 = dots[0][0], dots[0][1]
    x2, y2 = dots[1][0], dots[1][1]
    x3, y3 = dots[2][0], dots[2][1]
    x4, y4 = dots[3][0], dots[3][1]

    p1 = (x1, y1)
    p2 = (x2, y2)
    p3 = (x3, y3)
    p4 = (x4, y4)

    if gradient(p3, p1) == gradient(p4,p2):
        return 1
    elif gradient(p4,p3) == gradient(p2,p1):
        return 1
    else:
        return 0

dots=[[1, 4], [9, 2], [3, 8], [11, 6]]
print(solution(dots))

"""
정리 
수학 관련 문제 나오면 좀 더 오래걸리는 듯함

"""