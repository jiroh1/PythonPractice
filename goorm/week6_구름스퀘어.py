# N 개의 행사 예정
# 시작 시간 si 종료시간 ei 
# !!! 1의 시간이 지난 뒤에 다른 행사 시작 

# 최종답안
import sys
input = sys.stdin.readline

N = int(input())
events = []
for _ in range(N):
    s, e = map(int, input().split())
    events.append([s, e])
    
events.sort(key=lambda x : (x[1], x[0]))
count = end = 0
for s, e in events:
    if s > end:
        count += 1
        end = e
        
print(count)

# 첫 제출 답안, 실패
import sys

input = sys.stdin.readline

n = int(input())

ans = 0 
p = 0
for i in range(n):
	s, e = map(int, input().rstrip().split())
	if p + 1 <= s:
		ans += 1
		p = e
	
print(ans)





"""
예시1
입력
6
1 2
2 3
3 6
4 5
1 10
11 13
출력
3

예시2
입력
7
1 2
3 3
3 5
4 10
5 6
7 9
10 11
출력
5
"""