# 풀지 못함 리뷰 해야 함
import sys
input = sys.stdin.readline

N = int(input())
pair = []
cnt = [0 for _ in range(1000001)]
sticks = map(int, input().split())
for stick in sticks:
    cnt[stick] += 1

for length in range(1, 1000001):
    while cnt[length] > 1:
        cnt[length] -= 2
        pair.append(length)

pair.sort(reverse=True)
ans = 0
for i in range(1, len(pair), 2):
    ans += pair[i - 1] * pair[i]

print(ans)


"""
예시 1
입력
4
4 8 4 8
출력
32


예시2
입력
8
2 4 6 8 2 4 6 8
출력
56

예시3
입력
5
1 2 3 4 5
출력
0
"""