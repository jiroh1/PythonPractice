'''
Step1-2. 문제 먼저 직접 풀어보기 "체육복"
프로그래밍1
80 / 100.0 (2022.02.19)
문제 설명
점심시간에 도둑이 들어, 일부 학생이 체육복을 도난당했습니다. 다행히 여벌 체육복이 있는 학생이 이들에게 체육복을 빌려주려 합니다.
학생들의 번호는 체격 순으로 매겨져 있어, 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있습니다.
예를 들어, 4번 학생은 3번 학생이나 5번 학생에게만 체육복을 빌려줄 수 있습니다. 체육복이 없으면 수업을 들을 수 없기 때문에 체육복을 적절히 빌려 최대한 많은 학생이 체육수업을 들어야 합니다.

전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때,
체육수업을 들을 수 있는 학생의 최댓값을 return 하도록 solution 함수를 작성해주세요.

제한사항
전체 학생의 수는 2명 이상 30명 이하입니다.
체육복을 도난당한 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
여벌의 체육복을 가져온 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
여벌 체육복이 있는 학생만 다른 학생에게 체육복을 빌려줄 수 있습니다.
여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.

입출력 예
n	lost	reserve	   return
5	[2, 4]	[1, 3, 5]	5
5	[2, 4]	[3]	        4
3	[3]	    [1]	        2
입출력 예 설명
예제 #1
1번 학생이 2번 학생에게 체육복을 빌려주고, 3번 학생이나 5번 학생이 4번 학생에게 체육복을 빌려주면 학생 5명이 체육수업을 들을 수 있습니다.

예제 #2
3번 학생이 2번 학생이나 4번 학생에게 체육복을 빌려주면 학생 4명이 체육수업을 들을 수 있습니다.

'''

# 체육복 앞 , 뒤 번호만 빌려줄 수 있음.
# 전체학생 수 = n
# 체육복 도난당한 학생들의 번호가 담긴 배열 = lost
# 여벌의 체육복을 가져온 학생들의 번호 가 담긴 배열 = reverse
# 체육 수업들을 수 있는 학생의 수 를 return

#2< n < 30
# 1=<lost =<n 중복되는 번호 없
# 1=<reserve =<n 중복되는 번호 없


'''
case#1
n	lost	reserve	   return
5	[2, 4]	[1, 3, 5]	5
1,3,5 는 있어 근데, 여벌도 있으니깐 1이 2빌려주고, 3이나 5가 4 빌려주면됨
-> 
case#2 
n	lost	reserve	   return
5	[2, 4]	[3]	        4

1,3,5는 이미 있음 그니깐 이미 3명 가능
근데 2,4 둘중 한명이 없는데 3번이 있으니깐 2,4 둘중에 한명 가능함으로 4명

case#3
n	lost	reserve	   return
3	[3]	    [1]	        2

3 명중, 3번만 잃어버림 그니깐 우선 2명은 가능해
근데 , 여벌은 1번만 잇으니깐 3번을 입힐 순 없어

'''

'''
# 35% 
def solution(n, lost, reserve):
    answer = 0
    f_num = n-len(lost) #현 상황에서 수업을 들을 수 있는 학생의 수
    answer += f_num
    print(answer,'빌려주기 전')
    for i in range(len(reserve)):
        #print(reserve[i])
        if (reserve[i]-1) in lost:
            print((reserve[i]+1) , (reserve[i]-1))
            print(lost)
            print('find it!')
            answer += 1
    return answer
'''
'''
# 65%
def solution(n, lost, reserve):
    answer = 0
    f_num = n-len(lost) #현 상황에서 수업을 들을 수 있는 학생의 수
    answer += f_num
    for i in range(len(reserve)):
        print(reserve[i], '요소')
        if reserve[i] in lost: # reserve에 있는데 lost에 들어 갔을때
            print(reserve[i], ' 있네')
            lost.remove(reserve[i])
            print(lost,'있네lost')
            answer+=1
            if reserve[i] == 1:
                if 2 in lost:
                    answer += 1
                    lost.remove(2)
                    print(lost, ' 1일떄 lost')
                else :
                    pass
        elif reserve[i] > 1:
            if reserve[i]-1 in lost: #앞사람
                print(lost,' 1 이상 lost - 앞사람')
                answer += 1
                lost.remove(reserve[i]-1)
                print(lost,'last lost - 앞사람')
            elif reserve[i]+1 in lost: # 뒷사람
                print(lost,' 1 이상 lost - 뒷사람 ')
                answer += 1
                lost.remove(reserve[i]+1)
                print(lost,'last lost- 뒷사람 ')
        else:
            pass
    return answer
'''
'''
#75%
def solution(n, lost, reserve):
    answer = 0
    f_num = n-len(lost) #현 상황에서 수업을 들을 수 있는 학생의 수
    answer += f_num
    for i in range(len(reserve)):
        print(reserve[i], '요소')
        if reserve[i] == 1:
            if 2 in lost:
                answer += 1
                lost.remove(2)
                print(lost, ' 1일떄 lost')
            else :
                pass
        if reserve[i] in lost: # reserve에 있는데 lost에 들어 갔을때
            print(reserve[i], ' 있네')
            lost.remove(reserve[i])
            answer+=1

        elif reserve[i] > 1:
            if reserve[i]-1 in lost: #앞사람
                print(lost,' 1 이상 lost - 앞사람')
                answer += 1
                lost.remove(reserve[i]-1)
                print(lost,'last lost - 앞사람')
            elif reserve[i]+1 in lost: # 뒷사람
                print(lost,' 1 이상 lost - 뒷사람 ')
                answer += 1
                lost.remove(reserve[i]+1)
                print(lost,'last lost- 뒷사람 ')
        else:
            pass
    return answer
'''
# 80%
def solution(n, lost, reserve):
    answer = 0
    f_num = n-len(lost) #현 상황에서 수업을 들을 수 있는 학생의 수
    answer += f_num
    for i in range(len(reserve)):
        print(reserve[i], '요소')
        if reserve[i] in lost: # reserve에 있는데 lost에 들어 갔을때
            print(reserve[i], ' 있네')
            lost.remove(reserve[i])
            answer+=1
        elif reserve[i] == 1:
            if 2 in lost:
                answer += 1
                lost.remove(2)
                print(lost, ' 1일떄 lost')
            else :
                pass
        elif reserve[i] > 1:
            if reserve[i]-1 in lost: #앞사람
                print(lost,' 1 이상 lost - 앞사람')
                answer += 1
                lost.remove(reserve[i]-1)
                print(lost,'last lost - 앞사람')
            elif reserve[i]+1 in lost: # 뒷사람
                print(lost,' 1 이상 lost - 뒷사람 ')
                answer += 1
                lost.remove(reserve[i]+1)
                print(lost,'last lost- 뒷사람 ')
        else:
            pass
    return answer

#print(f'수업을 들을 수 있는 학생의 수는 {solution(30, [1,2],[1,2,3])}') #new case
#print(f'수업을 들을 수 있는 학생의 수는 {solution(5, [3],[5])}') #new case
#print(f'수업을 들을 수 있는 학생의 수는 {solution(5,[2, 4],[1, 3, 5])}') #case #1 #5
#print(f'수업을 들을 수 있는 학생의 수는 {solution(5,[2, 4],[1, 3, 5])}') #case #1 #5
#print(f'수업을 들을 수 있는 학생의 수는 {solution(5,[2, 4],[3])}') #case #2 답 4
#print(f'수업을 들을 수 있는 학생의 수는 {solution(3,[3],[1])}') #case #3 답 2
#print(f'수업을 들을 수 있는 학생의 수는 {solution(30,[2,3,5,7,29,30],[1,2,4,6])}') #new case
print(f'수업을 들을 수 있는 학생의 수는 {solution(10,[1,5,8,3,7],[7,5,2,9,6])}') #case #9