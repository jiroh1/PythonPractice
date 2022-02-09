'''
최대공약수와 최소공배수
https://programmers.co.kr/learn/courses/30/lessons/12940

문제 설명
두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성해 보세요. 배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다.
예를 들어 두 수 3, 12의 최대공약수는 3, 최소공배수는 12이므로 solution(3, 12)는 [3, 12]를 반환해야 합니다.

제한 사항
두 수는 1이상 1000000이하의 자연수입니다.

입출력 예
n	m	return
3	12	[3, 12]
2	5	[1, 10]

입출력 예 설명
입출력 예 #1
위의 설명과 같습니다.

입출력 예 #2
자연수 2와 5의 최대공약수는 1, 최소공배수는 10이므로 [1, 10]을 리턴해야 합니다.
'''


def solution(n, m):

    answer = []
    return answer

print(f"최대공약수와 최소공배수는 {solution(3,12)}")

'''
정리: 우선 최대공약수, 최소공배수 를 이해를 못했던 것 같음
아예 문제를 풀지 못하여 검색하여 답 확인 
answer = [] 이것만 보고 append 만 생각했던 것도 잘못된 요소 였던 듯


다른풀이:
case#1 with module
from math import gcd

# 최소공배수 구하는 함수
def lcm(n, m): 
    # 최소공배수는 두 수의 곱 // (최대공약수)를 하면 구해진다.
    return n * m // gcd(n, m)

def solution(n, m):
    
    # 최대공약수를 구해주는 라이브러리 gcd 사용
    return [gcd(n, m), lcm(n, m)]
    
case#2 
https://jisun-rea.tistory.com/entry/python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-Level1-%EC%B5%9C%EB%8C%80%EA%B3%B5%EC%95%BD%EC%88%98%EC%99%80-%EC%B5%9C%EC%86%8C%EA%B3%B5%EB%B0%B0%EC%88%98
#가장 내가 풀 수 있었을 법한 답안
def solution(n, m):
    a = n
    b = m
    if n>m:
        n, m = m, n
    while m%n:
        r = m%n
        m = n
        n = r
    return [n, a*b/n]

case#3
def gcdlcm(a, b):
    c, d = max(a, b), min(a, b)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
    answer = [c, int(a*b/c)]

    return answer
        
'''