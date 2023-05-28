# deposit, pay, reservation
# N 잔액, M 거래횟수

# 제출 답안
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int,input().split())

t = deque()

for _ in range(M):
	history = input().rstrip().split()
	if history[0] == 'deposit' :
		N += int(history[1])
		while len(t) > 0 and N >= int(t[0]):
			N -= int(t[0])
			t.remove(t[0])
	elif history[0] == 'pay' and N >= int(history[1]) :
		N -= int(history[1])
	elif history[0] == 'reservation':
		if N >= int(history[1]) and len(t) == 0 :
			N -= int(history[1])
		else:
			t.append(history[1])
	
print(N)


"""
예시1
입력
0 6
deposit 10
reservation 20
pay 5
deposit 10
deposit 10
reservation 6

출력
5

예시2
입력
0 6
deposit 10
pay 5
reservation 5
reservation 5
pay 5
deposit 10

출력
5

"""