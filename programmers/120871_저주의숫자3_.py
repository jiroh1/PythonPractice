"""
저주의 숫자3
https://school.programmers.co.kr/learn/courses/30/lessons/120871
"""
def solution (n):
    result = 0
    while n:
        # 3x inc
        while True:
            result += 1
            if result % 3 == 0 or '3' in str(result):
                pass
            else:
                break
        # cunter dec
        n-=1
    return result


n= 7
print(solution(n))

"""
정리
1. 처음에 3의 배수에 다가 1더하면 된다고 생각했는데, 4에서 5 넘어갈 때 뭔가 생각한거랑 달라서 고민했다.
2. 쉽게 숫자 '3'을 사용안하는 것도 표현할 수 있었으나, 3의 배수에만 꽂혀서 문제를 제대로 못 풀었던 문제

"""

"""
참고
https://www.youtube.com/watch?v=73kzECAq3CQ
"""