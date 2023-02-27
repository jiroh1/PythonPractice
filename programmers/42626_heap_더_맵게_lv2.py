"""
더 맵게
https://school.programmers.co.kr/learn/courses/30/lessons/42626
"""
import heapq
from  heapq  import *
def solution(scoville, K):
    answer=0
    heapq.heapify(scoville)
    while scoville[0]<K and len(scoville) > 1 :
        mix=heapq.heappop(scoville)+(heapq.heappop(scoville)*2)
        heapq.heappush(scoville,mix)
        answer += 1
    return answer if scoville[0]>=K else -1

# def solution(scoville, K):
#     count = 0
#     heapify(scoville)
#     while scoville[0] < K and len(scoville) > 1:
#         num1 = heappop(scoville)
#         num2 = heappop(scoville)
#         heappush(scoville, num1 + num2 * 2)
#         print('#',scoville)
#         count += 1
#     return count if scoville[0] >= K else -1        

if __name__ == "__main__":
    scoville = [1, 2, 3, 9, 10, 12]
    K=7 #	2
    print(solution(scoville,K))



"""
문제 설명
매운 것을 좋아하는 Leo는 모든 음식의 스코빌 지수를 K 이상으로 만들고 싶습니다. 
모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 Leo는 스코빌 지수가 가장 낮은 두 개의 음식을 아래와 같이 특별한 방법으로 섞어 새로운 음식을 만듭니다.

섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
Leo는 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복하여 섞습니다.
Leo가 가진 음식의 스코빌 지수를 담은 배열 scoville과 원하는 스코빌 지수 K가 주어질 때, 
모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 return 하도록 solution 함수를 작성해주세요.

제한 사항
scoville의 길이는 2 이상 1,000,000 이하입니다.
K는 0 이상 1,000,000,000 이하입니다.
scoville의 원소는 각각 0 이상 1,000,000 이하입니다.
모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return 합니다.

입출력 예
scoville	K	return
[1, 2, 3, 9, 10, 12]	7	2

입출력 예 설명
스코빌 지수가 1인 음식과 2인 음식을 섞으면 음식의 스코빌 지수가 아래와 같이 됩니다.
새로운 음식의 스코빌 지수 = 1 + (2 * 2) = 5
가진 음식의 스코빌 지수 = [5, 3, 9, 10, 12]

스코빌 지수가 3인 음식과 5인 음식을 섞으면 음식의 스코빌 지수가 아래와 같이 됩니다.
새로운 음식의 스코빌 지수 = 3 + (5 * 2) = 13
가진 음식의 스코빌 지수 = [13, 9, 10, 12]

모든 음식의 스코빌 지수가 7 이상이 되었고 이때 섞은 횟수는 2회입니다.
"""

"""
정리
## 정리

1. 제일 잊지말아야 할 점은 while 문에 대한 사용이다. 
    1. ‘`while scoville[0] < K:` ‘  를 사용하여 가장 작은 수가 기준보다 낮다면 계속 이라는 것을 하면 되는데, 
        for 문 만을 사용하다보니 while에 대한 것을 반대로 사용하려고 했다. 이것이 가장 큰 패착이었다.
2. 그 외에는 heapq 함수의 사용으로 구현하는 것만 하면된다.
"""