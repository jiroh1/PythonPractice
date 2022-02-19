'''
Step1-1. 문제 먼저 직접 풀어보기 "완주하지 못한 선수"
프로그래밍1
60 / 100.0 (2022.02.17)
문제 설명
수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.

마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

제한사항
마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
completion의 길이는 participant의 길이보다 1 작습니다.
참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
참가자 중에는 동명이인이 있을 수 있습니다.

입출력 예
participant	completion	return
["leo", "kiki", "eden"]	["eden", "kiki"]	"leo"
["marina", "josipa", "nikola", "vinko", "filipa"]	["josipa", "filipa", "marina", "nikola"]	"vinko"
["mislav", "stanko", "mislav", "ana"]	["stanko", "ana", "mislav"]	"mislav"
["leo","kiki", "kiki", "eden"]	["eden", "kiki","kiki"] "leo"
["leo","kiki", "kiki", "eden"]	["eden", "leo","kiki"] "kiki"

입출력 예 설명
예제 #1
"leo"는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.

예제 #2
"vinko"는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.

예제 #3
"mislav"는 참여자 명단에는 두 명이 있지만, 완주자 명단에는 한 명밖에 없기 때문에 한명은 완주하지 못했습니다.

'''


'''
case #1 30% 정답

def solution(participant, completion):
    answer = ''
    for i in range(len(participant)):
        cnt = participant.count(participant[i])
        if cnt >1: # list 안에 중복 있는 사람이면 그 사람을 먼저 넣고 return
            answer += participant[i]

        else: # list안에 중복 되는 사람이 없는 경우, 완주자 명단에 있는 지 확인 후 return
            for i in range(len(participant)):
                if participant[i] not in completion:
                    answer += participant[i]
            return answer
            
print(f'완주하지 못한 사람은 {solution(["leo","kiki", "kiki", "eden"],["eden", "kiki","kiki"] )}입니다.')
'''
'''
case #2 60 % 정
def solution(participant, completion):
    answer = ''
    for i in range(len(participant)):
        cnt = participant.count(participant[i])
        if cnt > 1:  # list 안에 중복 있는 사람이면 그 사람을 먼저 넣고 return
            answer += participant[i]

        else:  # list안에 중복 되는 사람이 없는 경우, 완주자 명단에 있는 지 확인 후 return
            a = set(participant)-set(completion)
            a = list(a)
            a = str(''.join(list(a)))
            answer += a
            return answer
#case #2-1
def solution(participant, completion):
    answer = ''
    for i in range(len(participant)):
        cnt = participant.count(participant[i])
        print(participant[i],'!',i)
        if cnt > 1:  # list 안에 중복 있는 사람이면 그 사람을 먼저 넣고 return
            #print('!up')
            answer += participant[i]
            while len(answer)>1:
                return answer


    else:  # list안에 중복 되는 사람이 없는 경우, 완주자 명단에 있는 지 확인 후 return
        a = set(participant)-set(completion)
        print(a,'set후')
        a = list(a)
        a = str(''.join(list(a)))
        print('!down')
        answer += a
        print(answer)
        return answer
문제풀이 및 코드 리뷰
개념학습 및 풀이 

print(f'완주하지 못한 사람은 {solution(["marina", "josipa", "nikola", "vinko", "filipa"],	["josipa", "filipa", "marina", "nikola"])}입니다.') # kiki 가 나와야함
'''
def solution(participant, completion):
    answer = ''
    for i in range(len(participant)):
        cnt = participant.count(participant[i])
        #print(participant[i],'!',i)
        if cnt > 1:  # list 안에 중복 있는 사람이면 그 사람을 먼저 넣고 return
            print(cnt,'!!!!cnt')
            #print('!up')
            answer += participant[i]
            # while len(answer) > 1:
            #     return answer
            # print(answer,'!')
            a = set(participant)-set(completion)
            print(a,'set후')
            a = list(a)
            a = str(''.join(list(a)))
            print('!down')
            answer += a
            b= len(answer)/2
            print(answer[:int(b)])
            answer = answer[:int(b)]
    else :
        a = set(participant) - set(completion)
        print(a, 'set후')
        a = list(a)
        a = str(''.join(list(a)))
        print('!down')
        answer += a

    return answer
#print(f'완주하지 못한 사람은 {solution(["marina", "josipa", "nikola", "vinko", "filipa"],	["josipa", "filipa", "marina", "nikola"])}입니다.') # kiki 가 나와야함
#print(f'완주하지 못한 사람은 {solution(["leo","kiki", "kiki", "eden"],["eden", "kiki","kiki"] )}입니다.')
#print(f'완주하지 못한 사람은 {solution(["leo","kiki", "kiki", "eden"],["eden", "leo","kiki"])}입니다.')
print(f'완주하지 못한 사람은 {solution(["mislav", "stanko", "mislav", "ana"],	["stanko", "ana", "mislav"])}입니다.')





import numpy as np
# arr1 = ["leo","kiki", "kiki", "eden"]
# arr2 = ["eden", "kiki"]
#
# a = set(arr1) - set(arr2)
# a = list(a)
# print(a, type(a))

# def solution(participant, completion):
#     answer = []
#     part= np.array(participant)
#     comp =np.array(completion)
#     print(part, type(part))
#     print(comp, type(comp))
#     a= part-comp
#     a=list(a)
#     print(type(a))
#     print(a.tolist())
#
#
#
# print(f'완주하지 못한 사람은 {solution(["leo","kiki", "kiki", "eden"],["eden", "kiki","kiki"] )}입니다.')

# arr1 = np.array([10, 5, 3, 7, 1, 5])
# arr2 = np.array([10, 5, 3, 7, 1, 5])
#
# print(f'numpy array 끼리 덧셈 = {arr1 + arr2}')
# print(f'numpy array 끼리 뺄셈 = {arr1 - arr2}')
# print(f'numpy array 끼리 곱셈 = {arr1 * arr2}')
# print(f'numpy array 끼리 나눗셈 = {arr1 / arr2}')
# arr1=list(arr1)
# print(arr1,'!',type(arr1))
# arr1.tolist()
# print(arr1,type(arr1))

'''


a = np.array([1.2, 3.4, 5.6, 7.8])
b = np.array([[1, 3], [5, 7]])
print(a) #[1.2 3.4 5.6 7.8]
print(list(a)) # [1.2, 3.4, 5.6, 7.8]
print(a.tolist()) # [1.2, 3.4, 5.6, 7.8]

list(b) # [array([1, 3]), array([5, 7])]
b.tolist() # [[1, 3], [5, 7]]
'''
'''
정리 : 1.  if _ in list 로 list 안에 있는지 확인
https://zetawiki.com/wiki/Python_%EB%A6%AC%EC%8A%A4%ED%8A%B8_%EC%9A%94%EC%86%8C_%ED%8F%AC%ED%95%A8%EC%97%AC%EB%B6%80_%ED%99%95%EC%9D%B8_in
2. count 함수로 list 안에 중복값 찾기
https://velog.io/@haileeyu21/TIL-Python-%EB%A6%AC%EC%8A%A4%ED%8A%B8-%EC%A4%91%EB%B3%B5-%EC%9A%94%EC%86%8C-%EA%B0%9C%EC%88%98-%EC%B0%BE%EA%B8%B0-%EC%A0%9C%EA%B1%B0-%EC%82%AD%EC%A0%9C

'''