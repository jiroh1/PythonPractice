""""
문자열밀기
https://school.programmers.co.kr/learn/courses/30/lessons/120921
"""

def solution(A, B):
    if A == B:
        return 0
    for i in range(len(A)):
        mid=A[-i:]+A[:-i]
        if mid == B:
            return i
        else:
            pass
    return -1

A='hello'
B='ohell'
print(solution(A,B))


"""
정리
1. 단순 구현일 것 같았는데, 채점에서 실패 케이스가 있어서 정리 해봄
2. 조건 "atat"는 오른쪽으로 한 칸, 세 칸을 밀면 "tata"가 되므로 최소 횟수인 1을 반환합니다.
 -> 이것에 대해서 그냥 return 을 1로 먼저 시도 했는데 ,안된 후 i로 진행하니 바로 해결
3. 다른 풀이보다 나의 풀이가 좀 이해가 잘 되는 문제
"""
"""
다른풀이
# case 1 
solution=lambda a,b:(b*2).find(a)
-> lambda 여서 적어봄
"""