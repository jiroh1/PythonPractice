'''
정수 제곱근 판별
https://programmers.co.kr/learn/courses/30/lessons/12934
문제 설명
임의의 양의 정수 n에 대해, n이 어떤 양의 정수 x의 제곱인지 아닌지 판단하려 합니다.
n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, n이 양의 정수 x의 제곱이 아니라면 -1을 리턴하는 함수를 완성하세요.

제한 사항
n은 1이상, 50000000000000 이하인 양의 정수입니다.

입출력 예
n	return
121	144
3	-1

입출력 예 설명
입출력 예#1
121은 양의 정수 11의 제곱이므로, (11+1)를 제곱한 144를 리턴합니다.

입출력 예#2
3은 양의 정수의 제곱이 아니므로, -1을 리턴합니다.
'''
# 간결하게 만든 답


def solution(n):
    sqrt = int(n**(1/2)) # 제곱근
    if (sqrt * sqrt) == n: # 제곱근 곱해서 다시 n이 되는 값인지로 확인
        return (sqrt+1)**2 # 맞으면 제곱근 +1
    return -1


print(solution(121))

'''
# 처음 풀었던 답 
def solution(n):
    answer = 0
    sqrt = int(n**(1/2))
    if (sqrt * sqrt) == n:
        answer += (sqrt+1)**2
    else:
        return -1
    return answer 
'''
#
# print(int(3**(1/2)) ,'exam')
# print(int(3**(2)) ,'exam2')

'''
정리:
1. 제곱근 계산 방법 - https://needneo.tistory.com/77
2. 생각보다 어렵지 않았고, 최대한 코드를 짧고 간략하게 쓰는 연습을 해보았다. 

다른 풀이:
case#1
def nextSqure(n):
    sqrt = n ** (1/2)

    if sqrt % 1 == 0:
        return (sqrt + 1) ** 2
    return 'no'
    
case#2
def nextSqure(n):
    return n == int(n**.5)**2 and int(n**.5+1)**2 or 'no'    
    
case#3
def nextSqure(n):
    from math import sqrt
    return "no" if sqrt(n) % 1 else (sqrt(n)+1)**2
    
case#4
import math
def nextSqure(n):
    # 함수를 완성하세요
    return 'no' if not math.sqrt(n).is_integer() else (math.sqrt(n)+1)**2
# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(nextSqure(121)));


'''
def solution(n):
    answer = 0
    sqrt = int(n**(1/2))
    if (sqrt * sqrt) == n:
        answer += (sqrt+1)**2
    else:
        return -1
    return answer


print(solution(121))

def solution(n):
    sqrt = int(n**(1/2))
    if (sqrt * sqrt) == n:
        return (sqrt+1)**2
    return -1
