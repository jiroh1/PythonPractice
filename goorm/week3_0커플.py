# 시뮬레이션과 창의적 해결법

# 제출 답안
import sys

input=sys.stdin.readline

n = int(input())
human = list(map(int, input().split(' ')))

print(sum(human))

"""
정리
답은 간단하게 제시했지만, 해설 중에 hash table에 대한 개념이 있어서 정리

# hash 기반 자료구조 이용

N = int(input())
S = list(map(int, input().split()))

occur = dict()
for i in range(N):
    # 현재 점수가 존재하는지를 occur에 기록해둡니다.
    occur[S[i]] = 1

ans = 0
for i in range(N):
    # 각 점수마다 부호가 반대인 점수 값이 occur에 존재하는지를 확인합니다.
    # key 값이 존재하는 경우에는 소개팅을 진행할 수 있다는 뜻이니, 넘어가줍시다.
    if -S[i] not in occur:
        ans += S[i]
        
print(ans)

# 절대값의 개수를 이용


N = int(input())
S = list(map(int, input().split()))

occur = [0 for _ in range(200001)]
for i in range(N):
    # abs 함수는 인자로 들어온 수의 절댓값을 반환하는 함수입니다.
    occur[abs(S[i])] += 1

ans = 0
for i in range(1, 200001):
    if occur[i] != 1:
        continue
    for j in range(N):
        if abs(S[j]) == i:
            ans += S[j]
        
print(ans)
"""