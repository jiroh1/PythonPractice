# 크기 K
# push :stack 에 크기가 1인 정수를 추가하는 명령 , 이미 가득 차있을 때 push Overflow출력
# pop : 가장 최근에 추가된 정수를 제거 , 제거 된 정수를 출력 , 이미 비어 있으면 Underflow

# N 명령의 개수

import sys

input = sys.stdin.readline

N, K = map(int,input().split())
command=[list(input().split()) for _ in range(N)]
stack=[]
for i in range(N):
	if command[i][0] == 'push' and len(stack) >= K :
		print('Overflow')
	elif command[i][0] == 'push' and len(stack) < K :
		stack.append(command[i][1])
	elif command[i][0] == 'pop' and len(stack) == 0:
		print('Underflow')
	elif command[i][0] == 'pop':
		print(stack.pop())

"""
예시1
입력
10 3
push 1
push 6
push 5
pop
pop
pop
push 4
push 4
push 3
pop

출력
5
6
1
3

예시2
입력
5 3
pop
push 4
push 9
push 9
push 2

출력
Underflow
Overflow
"""