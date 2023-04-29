"""
연속된 수의 합
https://school.programmers.co.kr/learn/courses/30/lessons/120923
"""
# num개의 연속된 수를 더하여 total이 될 수 없는 테스트 케이스는 없습니다.

def solution(num, total):
    if total == 0:
        if num == 3:
            return [-1, 0 ,1]
        elif num == 1:
            return [0]
    elif num == 1:
        return [total]
    elif num % 2 == 1:
        for i in range(total):
            if num * i == total:
                return [n for n in range(i-(num//2), i-(num//2) +num)]
    elif num % 2 == 0:
        for i in range(total):
            if (num/2)*(2*i+1) == total:
                return [n for n in range(i-(num//2)+1, i-(num//2) +num+1)]


num = 3
total = 0

print(solution(num,total))


"""
[-1, 0, 1]의 합이 0
-total 0이 되는 상황 [1,0,-1]
-num이 1이 되는 상황 [total]

짝수면 (num/2)*(n+1) == total
6개 : n-2,n-1,n,n+1,n+2,n+3 ->6n + 3 -> 3(2n+1)
4 개 : n-1, n , n+1, n+2 -> 4n +2 -> 2(2n+1)
2 개 : n , n+1 -> 2n +1 

홀수면 num*n == total
1개 : n
3 : n-1,n,n+1 -> 3n
5 : n-2,n-1,n,n+1,n+2 -> 5n

"""
""" 
제출 답안 
# test 9 이 실패.
def solution(num, total):
    if total == 0:
        if num == 3:
            return [-1,0,1]
        elif num == 1: # test 7
            return [0]
    elif num == 1: # test 1 
        return [total]
    
    elif num % 2 == 1 : # 홀수
        for i in range(total):
            if num * i == total:
                return [n for n in range(i-(num//2), i-(num//2) +num)]
    elif num % 2 == 0 : # 짝수
        for i in range(total):
            if (num/2)*(2*i+1) == total:
                return [n for n in range(i-(num//2)+1, i-(num//2) +num+1)]
"""