'''
체육복
https://programmers.co.kr/learn/courses/30/lessons/42862
'''
def solution(n, lost, reserve):
    answer = 0
    f_num = n-len(lost) #현 상황에서 수업을 들을 수 있는 학생의 수
    answer += f_num
    reserve = sorted(reserve)
    lost = sorted(lost)
    for r in reserve[:]:
        if r in lost: # reserve에 있는데 lost에 들어 갔을때
            lost.remove(r)
            reserve.remove(r)
            answer+=1
    for i in range(len(reserve)):
        if reserve[i]-1 in lost: #앞사람
            answer += 1
            lost.remove(reserve[i]-1)
        elif reserve[i]+1 in lost: # 뒷사람
            answer += 1
            lost.remove(reserve[i]+1)
    return answer

#print(f'수업을 들을 수 있는 학생의 수는 {solution(30, [1,2],[1,2,3])}') #new case
#print(f'수업을 들을 수 있는 학생의 수는 {solution(5, [3],[5])}') #new case
#print(f'수업을 들을 수 있는 학생의 수는 {solution(5,[2, 4],[1, 3, 5])}') #case #1 #5
#print(f'수업을 들을 수 있는 학생의 수는 {solution(5,[2, 4],[1, 3, 5])}') #case #1 #5
#print(f'수업을 들을 수 있는 학생의 수는 {solution(5,[2, 4],[3])}') #case #2 답 4
#print(f'수업을 들을 수 있는 학생의 수는 {solution(3,[3],[1])}') #case #3 답 2
#print(f'수업을 들을 수 있는 학생의 수는 {solution(30,[2,3,5,7,29,30],[1,2,4,6])}') #new case
print(f'수업을 들을 수 있는 학생의 수는 {solution(10,[1,5,8,3,7],[7,5,2,9,6])}') #case #9

def soution(n, lost, reserve): # greedy 탐욕법 사용 ( N 이 적기 떄문에 사용가능)
    u = [1]*(n+2)
    for i in reserve:
        u[i] += 1
    for i in lost:
        u[i] -= 1
    for i in range(1,n + 1):
        if u[i - 1] == 0 and u[i] == 2:
            u[i - 1:i + 1] = [1, 1]
        elif u[i] == 2 and u[i+1] == 0:
            u[i:i+2] = [1, 1]
    return len([x for x in u[1:-1] if x > 0])


def solution_h(n, lost, reserve): #set을 이용하여  Sorted(r) 부분으로 인하여 O(klogk) 의 복잡도를 가진다. 여벌의 체육복을  가져온 학생들만 확인 하기 떄문에
    s = set(lost) & set(reserve)
    l = set(lost) - s
    r = set(reserve) - s
    for x in sorted(r):
        if x - 1 in l:
            l.remove(x - 1)
        elif x +1 in l:
            l.remove(x + 1)
    return n - len(n)
