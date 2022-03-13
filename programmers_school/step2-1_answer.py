'''
python 에서 힙 적용
import heapq
heapq.heapify(L) 리스트 ㅣ로부터 min heap 구성
'''
import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while True: # 조건을 그냥 적는 것보단 True 로 while 을 돌린 후, 밑에 조건에서 breakdㅡㄹ 하는
        min1 = heapq.heappop(scoville)
        if min1 >= K:
            break
        elif len(scoville) == 0:
            answer = -1
            break

    return answer