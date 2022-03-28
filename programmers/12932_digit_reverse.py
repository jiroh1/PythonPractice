'''
자연수 뒤집어 배열로 만들기
https://programmers.co.kr/learn/courses/30/lessons/12932

문제 설명
자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.

제한 조건
n은 10,000,000,000이하인 자연수입니다.

입출력 예
n	return
12345	[5,4,3,2,1]
'''


def solu(n):
    n = str(n)
    answer = []
    for i in range(len(n)):
        answer.append(int(n[i]))
    answer = sorted(answer,reverse=True)
    return answer


def solution(n):
    answer = []
    s = reversed(str(n))
    for i in s:
        answer.append(int(i))
    return answer

print(solu(12345)==solution(12345),'compare')
print(solu(1000020),'solu')
print(solution(1000020),'solution')
# print(solution(10000000000))


d = 12345
d = reversed(str(d))
'''
첫풀이 :
def solu(n):
    n = str(n)
    answer = []
    for i in range(len(n)):
        answer.append(int(n[i]))
    answer = sorted(answer,reverse=True)
    return answer
-> 테케는 통과했으나, 코드가 통과가 안됨. sorted로 할 경우, 말그대로 숫자의 크기로 정렬 하는데, 이 문제는 그냥 reverse를 요구하는 문제네요
'''
'''
n = 1000020
[2, 1, 0, 0, 0, 0, 0] #sorted 후 
[0, 2, 0, 0, 0, 0, 1] #reversed

'''

'''
다른 풀이:
# case01
def digit_reverse(n):
    return list(map(int, reversed(str(n))))
    
   
# case02
def digit_reverse(n):
    return [int(i) for i in str(n)][::-1]
    
# case03

def digit_reverse(n):
    # 함수를 완성해 주세요
    ret =[]
    for i in str(n):
        ret.append(int(i))
    ret.reverse() 
    return ret
     
'''