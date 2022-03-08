'''
Step1-3. 문제 먼저 직접 풀어보기 "여행경로"

문제 설명
주어진 항공권을 모두 이용하여 여행경로를 짜려고 합니다. 항상 "ICN" 공항에서 출발합니다.

항공권 정보가 담긴 2차원 배열 tickets가 매개변수로 주어질 때, 방문하는 공항 경로를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

제한사항
모든 공항은 알파벳 대문자 3글자로 이루어집니다.
주어진 공항 수는 3개 이상 10,000개 이하입니다.
tickets의 각 행 [a, b]는 a 공항에서 b 공항으로 가는 항공권이 있다는 의미입니다.
주어진 항공권은 모두 사용해야 합니다.
만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 합니다.
모든 도시를 방문할 수 없는 경우는 주어지지 않습니다.
입출력 예
tickets
[["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
return
["ICN", "JFK", "HND", "IAD"]

tickets
[["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
return
["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]

입출력 예 설명
예제 #1
["ICN", "JFK", "HND", "IAD"] 순으로 방문할 수 있습니다.

예제 #2
["ICN", "SFO", "ATL", "ICN", "ATL", "SFO"] 순으로 방문할 수도 있지만 ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"] 가 알파벳 순으로 앞섭니다.
'''

# ticket 수 +1 = 방문한 곳의 길이

def solution(tickets):
    answer = ['ICN']
    #ICN 다음 목적지 찾
    first_destination = []
    if len(answer) < 2:
        for i in range(len(tickets)):
            if tickets[i][0] == "ICN":
                start_index = i
                first_destination.append(tickets[start_index][1])
                first_destination = sorted(first_destination)
        answer.append(first_destination[0])
        tickets.remove(tickets[start_index])
        print('인천 후 ', tickets)
    print('중간', answer)
    s = 0
    while s <= len(tickets):
        s += 1
        if len(answer) > 1:
            print('='*30)
            print('들어왓어 > 2 ')
            print('들어와서 answer ', answer)
            compare_des = []
            for j in range(len(tickets)):
                if answer[-1] == tickets[j][0]:
                    print('answer 가장 마지막 :',answer[-1],j, tickets[j] ) #,f'찾았어 {s} 목적지 '
                    print(tickets[j][1],f'넣을것 {j}',tickets[j])
                    compare_des.append(tickets[j][1])
                    compare_des = sorted(compare_des)
                    print('마지막에 따라 넣은 것들 : ',compare_des)
        answer.append(compare_des[0])
        print('* delete ticket :' , j, tickets[j])
        # print('all : ', tickets)
        # tickets.remove(delete)
        print('* all after delete tickets : ',tickets)

        print(answer,'!!2nd check')

    return answer


# def solution(tickets):
#     answer = []
#     direction = {}
#     for t in tickets:
#         direction[t[0]] = direction.get(t[0], []) + [t[1]]
#
#     for d in direction:
#         direction[d].sort(reverse=True)
#     visiting = ['ICN']
#     while visiting:
#         from_location = visiting[-1]
#         print('from_location', from_location)
#         if from_location not in direction or len(direction[from_location]) == 0:
#             answer.append(visiting.pop())
#             # print('answer', answer)
#         else:
#             visiting.append(direction[from_location][-1]) # 알파벳 순서에서 맨 앞
#             direction[from_location].pop()
#     answer = [i for i in answer[::-1]]
#     return answer
#
#
# from copy import deepcopy
#
# def dfs(v, edge):
#     if v not in edge.keys():
#         return [v]
#     if len(edge[v]) == 1:
#         edge2 = deepcopy(edge)
#         del edge2[v]
#         return [v] + dfs(edge[v][0], edge2)
#
#     li = []
#
#     for value in edge[v]:
#         edge2 = deepcopy(edge)
#         edge2[v].remove(value)
#         li.append(dfs(value, edge2))
#
#     m = 0
#     idx = 0
#     for i in range(len(li)):
#         l = len(li[i])
#         if l > m:
#             m = l
#             idx = i
#
#     return [v] + li[idx]
#
#
# def solution(tickets):
#     edge = {}
#
#     for v in tickets:
#         edge[v[0]] = edge.get(v[0], []) + [v[1]]
#
#     for v in edge.values():
#         v.sort()
#
#     return dfs('ICN', edge)


#
# from collections import deque, defaultdict
#
#
# def solution(tickets):
#     graph = defaultdict(list)
#     START = "ICN"
#     route = []
#     for start, end in sorted(tickets, reverse=True):
#         graph[start].append(end)
#
#     def dfs(to):
#         while graph[to]:
#             dfs(graph[to].pop())
#         route.append(to)
#     dfs(START)
#     return route[::-1]

# print(f'가능 경로는 {solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])}')
print(f'가능 경로는 {solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])}')
# print("ATL"<"SFO") #True



'''
#1st submit :50%
def solution(tickets):
    answer = []
    #ICN 찾기
    for i in range(len(tickets)):
        # print(tickets[i][0])
        if tickets[i][0] == "ICN":
            start_index = i
            print(start_index,tickets[start_index], '찾았다 Icn')
            answer.append(tickets[start_index][0])
            answer.append(tickets[start_index][1])
    # 다음 목적지 찾기
    for j in range(len(tickets)):
        if tickets[start_index][1] == tickets[j][0]:
            second_index = j
            print(second_index,tickets[second_index], '찾았어 2nd 목적')
            answer.append(tickets[second_index][1])
    #그 다음 목적지 찾기
    for k in range(len(tickets)):
        if tickets[second_index][1] == tickets[k][0]:
            third_index = k
            print(third_index, tickets[third_index], '찾았어 3rd 목적지')
            answer.append(tickets[third_index][1])

    return answer

'''