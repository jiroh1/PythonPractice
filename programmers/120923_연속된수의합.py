"""
연속된 수의 합
https://school.programmers.co.kr/learn/courses/30/lessons/120923
"""
# 제출답안    
def solution(num, total):
    x = (total - sum([i for i in range(0,num)])) // num
    return [n for n in range(x,x+num)]

num = 3
total = 0

print(solution(num,total))


"""
정리
#  홀수 x,x+1,x+2 = total 3x + range(0,num)
# 홀수 x,x+1,x+2,x+3,x+4 - total 5x + range(0,num)
# 짝수 x,x+1,x+2,x+3 = total = 4x +2 
# total = num * x + range(0,num)
1. 기존에는 중심을 x로 두었다면, 이번에는 그냥 x를 구해버려서 그냥 범위 num을 더해서 구했다.
2. 1번 같이 해도 해결이 될 수도 있었겠지만, 헷갈리는 부분이 생겼던 것 같다.
3. 찾아 보지 않고 시간이 지난 후 다시 풀었더니 금방 풀림 단순하게 생각하자.
"""


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

# num개의 연속된 수를 더하여 total이 될 수 없는 테스트 케이스는 없습니다.

def solution(num, total):
    if num % 2 == 1 :
        for i in range(total):
            if num * i == total:
                return [n for n in range(i-(num//2), i-(num//2) +num)]
    elif num % 2 == 0:
        for i in range(total):
            if (num/2)*(2*i+1) == total:
                return [n for n in range(i-(num//2)+1, i-(num//2) +num+1)]

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
