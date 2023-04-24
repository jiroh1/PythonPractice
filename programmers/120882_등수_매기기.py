"""
등수 매기기
https://school.programmers.co.kr/learn/courses/30/lessons/120882
"""

# 제출답안
def solution(score):
    answer = []
    avg_list=[ sum(i)/ 2 for i in score]

    sorted_avg_list=sorted(avg_list, reverse=True)
    for i in avg_list:
        answer.append(sorted_avg_list.index(i)+1)

    return answer


score=[[80, 70], [90, 50], [40, 70], [50, 80]]

print(solution(score))

""" 
정리
1. 헷갈릴 것 같아서 작성했는데, 생각보다 쉽게 풀렸다.
2. case 1 처럼 enumerate 해도되고 내 코드를 조금 더 간략하게 할 수 있는 것이 case2 인 것 같다.
"""
"""
다른풀이
# case 1
def solution(score):
    rank = sorted([sum(s) / 2 for s in score], reverse=True)
    rankDict = {}
    for i, r in enumerate(rank):
        if r not in rankDict.keys():
            rankDict[r] = i + 1
    return [rankDict[sum(s) / 2] for s in score]

# case 2 
def solution(score):
    a = sorted([sum(i) for i in score], reverse = True)
    return [a.index(sum(i))+1 for i in score]
"""