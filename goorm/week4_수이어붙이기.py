# 최종 제출 답안
from itertools import permutations

N = int(input())
A = list(map(int, input().split()))
A.sort()

ans = 1e18
for order in permutations(A, N):
	print(order)
	cur = order[0]
	for i in range(1, N):
		if cur % 10 == order[i] // 10:
				cur = cur * 10 + order[i] % 10 # 겹치는 것이 나오면 이렇게 뿥이는 것
		else:
				cur = cur * 100 + order[i]
				
	ans = min(ans, cur)

print(ans)
# 맨 아래에 예시 있음

'''
# 첫 제출 답안
# A 가 적힌 카드 N 
# 순서대로 이어붙여서
# 가장 작은수 
import sys
input=sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))

a=[]
b=[]
for i in range(N):
	for j in range(N):
		if str(A[i])[-1] == str(A[j])[0]:
			a.append(A[j])
			b.append(A[i])
a = sorted(a)
b = list(set(b))
c = [x for x in A if x not in a+b]

print(''.join(list(map(str,list(set(a+b+c))))))
'''		


"""
예시1
입력
4
42 31 16 19
출력
1631942

예시2
입력
2
87 88
출력
887

"""

"""
order,ans: (16, 31, 19, 42) 16193142
cur: 16
cur: 1631
cur,cur%10,order[i],order[i]//10: 1631 / 1 / 19 1
cur 16319
order,ans: (16, 31, 42, 19) 1631942

"""