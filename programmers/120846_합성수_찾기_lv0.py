"""
합성수 찾기
https://school.programmers.co.kr/learn/courses/30/lessons/120846
"""
n=10

def solution(n):
    answer = 0
    for i in range(n+1):
        c = 0
        for j in range(1, i+1):
            print('j',j)
            if i % j == 0:
                c+=1
        if c >= 3:
                answer += 1
    return answer

print(solution(n))
"""
다른풀이

def solution(n):
    output = 0
    for i in range(4, n + 1):
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                output += 1
                break
    return output
"""

"""
정리

합성수. 약수의 개수가 3개 이상인 수를 말한다. -> 약수의 개수가 몇 개 인지 판별하면 된다.
 수학에 대한 논리가 들어가면 풀이가 좀 안되는 경우가 많은 듯 하다.

다른풀이 에서 처럼 우선 첫 range 도 4 이후. ( 1,2,3은 합성수가 아니니)
두 번째 for loop 에서 int(i**0.5)에 대해서는 제곱근 이하의 약수하나와 이상의 약수 하나씩 이루어지니깐 한번만 나누면 되니깐 나누는 숫자의 범위를 줄인 것임
"""