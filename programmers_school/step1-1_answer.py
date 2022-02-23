from collections import Counter


def solution(participant, completion):
    answer = ''

    x_participant = Counter(participant)
    y_completion = Counter(completion)

    answer = list(x_participant - y_completion)[0]

    return answer

def solution(participant, completion):
    d={}
    for x in participant:
        d[x] = d.get(x,0) + 1
        print(d[x],'dx',d)
    for x in completion:
        d[x] -= 1
    dnf = [k for k,v in d.items() if v >0]
    answer = dnf[0]
    return answer
#print(f'완주하지 못한 사람은 {solution(["marina", "josipa", "nikola", "vinko", "filipa"],	["josipa", "filipa", "marina", "nikola"])}입니다.') # kiki 가 나와야함
#print(f'완주하지 못한 사람은 {solution(["leo","kiki", "kiki", "eden"],["eden", "kiki","kiki"] )}입니다.')
#print(f'완주하지 못한 사람은 {solution(["leo","kiki", "kiki", "eden"],["eden", "leo","kiki"])}입니다.')
print(f'완주하지 못한 사람은 {solution(["mislav", "stanko", "mislav", "ana"],	["stanko", "ana", "mislav"])}입니다.')

def solution(participant,completion): # 정렬을 이용함  O(NlogN) 테스트는 통과하지만,
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[len(participant)-1]

