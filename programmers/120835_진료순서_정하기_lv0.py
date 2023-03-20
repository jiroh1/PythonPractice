"""
진료순서 정하기
https://school.programmers.co.kr/learn/courses/30/lessons/120835
emergency=[3, 76, 24]
result
[3, 1, 2]
emergency=[1, 2, 3, 4, 5, 6, 7]
result
[7, 6, 5, 4, 3, 2, 1]
emergency=[30, 10, 23, 6, 100]
result
[2, 4, 3, 5, 1]
"""
# 제출답안
def solution(emergency):
    line=sorted(emergency,reverse=True)
    return [line.index(i)+1 for i in emergency]


if __name__=='__main__':
    emergency=[3, 76, 24]
    print(solution(emergency))

"""
정리
처음에 dict 형태로 풀려고 했으나 index() 를 사용하면됨
"""