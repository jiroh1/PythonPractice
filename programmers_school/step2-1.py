'''
Step1-1. 문제 먼저 직접 풀어보기 "더 맵게"

문제 설명
매운 것을 좋아하는 Leo는 모든 음식의 스코빌 지수를 K 이상으로 만들고 싶습니다.
모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 Leo는 스코빌 지수가 가장 낮은 두 개의 음식을 아래와 같이 특별한 방법으로 섞어 새로운 음식을 만듭니다.

섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
Leo는 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복하여 섞습니다.
Leo가 가진 음식의 스코빌 지수를 담은 배열 scoville과 원하는 스코빌 지수 K가 주어질 때, 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는
최소 횟수를 return 하도록 solution 함수를 작성해주세요.

제한 사항
scoville의 길이는 2 이상 1,000,000 이하입니다.
K는 0 이상 1,000,000,000 이하입니다.
scoville의 원소는 각각 0 이상 1,000,000 이하입니다.
모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return 합니다.

입출력 예
scoville	            K	 return
[1, 2, 3, 9, 10, 12]	7	 2

입출력 예 설명
스코빌 지수가 1인 음식과 2인 음식을 섞으면 음식의 스코빌 지수가 아래와 같이 됩니다.
새로운 음식의 스코빌 지수 = 1 + (2 * 2) = 5
가진 음식의 스코빌 지수 = [5, 3, 9, 10, 12]

스코빌 지수가 3인 음식과 5인 음식을 섞으면 음식의 스코빌 지수가 아래와 같이 됩니다.
새로운 음식의 스코빌 지수 = 3 + (5 * 2) = 13
가진 음식의 스코빌 지수 = [13, 9, 10, 12]

모든 음식의 스코빌 지수가 7 이상이 되었고 이때 섞은 횟수는 2회입니다.
'''

'''
1/ 조합을 해서 k 이상이 나오게 하기 이게 우선
2. 

'''
#  스코빌 지수 를 > k : -1

# D =[]
# while len(D)== 0:
#     A = [1, 13, 9, 10, 12]
#     B = [1, 2, 3, 4, 5, 6]
#     D = [i for i, j in zip(A, B) if i == j]
#     if len(D) == 0 :
#         print(D)
#         break
#     else :
#         print('d',D)
#         print('wow')

# k= 7
# a=[]
# for i in range(1,k) :
#     a.append(i)
# print(a)
# a = list(set(a)-set([0]))
# print(a)

def solution(scoville, K):
    scoville = sorted(scoville)
    answer = 0
    fail = []
    for i in range(1,K):
        fail.append(i)
    print(fail,'fail')
    a = 0
    while True :
        if a >1000000:
            break
        a += 1
        # 스코빌 지수를 K이상으로 만들 수 없는 경우
        if len(scoville) == 1:
            if K in scoville:
                pass
            else:
                return -1

        # scoville 안에 스코빌 지수 아래의 수가 있는지 확인
        gap = list(set(fail) - set(scoville))
        #print(gap,'1st_gap')
        if len(gap) == len(fail):
            break
        # cal 이라는 곳에 scoville 에 있는 가장 작은 수를 받아서 연산 후 다시 scovile에 넣어준다.
        # cal = []
        # cal.append(scoville.pop(0))
        # cal.append(scoville.pop(0))
        result = scoville[0] + scoville[0] * 2
        scoville.append(result)
        scoville = sorted(scoville)
        print(scoville,'sco',a,'a')
        # print(gap, 'gap',a)
        answer += 1


    return answer

#print(f'횟수는 : {solution([1, 2, 3, 9, 10, 12],7)}회')
#print(f'횟수는 : {solution([1,1,1,1,1,1,11,1,1,1,1,11,1,1,1,1,1,1,1],23)}회')
#print(f'횟수는 : {solution([1,1],8)}회')
print(f'횟수는 : {solution([6,7,8],7)}회')
#print(f'횟수는 : {solution([],)}회')

#
# s = [1, 2, 3, 9, 10, 12]
# #스코빌 지수 K 이상 만들 경우
# fail =[1,2,3,4,5,6]
#
# i =0
# try :
#     while fail[i] < 7:
#         i += 1
#         print('re')
# except:
#     print('done')


# scovile 수 계산
# cal = []
# cal.append(s.pop(0))
# cal.append(s.pop(0))
# result = cal[0] + cal[1]*2
# s.append(result)
# s = sorted(s)
#
#
# cal = []
# cal.append(s.pop(0))
# cal.append(s.pop(0))
# result = cal[0] + cal[1]*2
# s.append(result)
# s = sorted(s)
#
#
# print(result,'result')
# print(cal)
# print(s)



# 파이썬 리스트 비교  https://calssess.tistory.com/91

# A = [1, 2, 3, 4, 5, 6]
# B = [9, 8, 7, 6, 5]
#
# D = [i for i, j in zip(A, B) if i != j]
#
# print(D)
#
# s = [ 9, 10, 12]
# fail = [1, 2, 3, 4, 5, 6]
#
# f = list(set(fail) - set(s))
# print(len(f))
#
# if len(f) == 6:
#     print('done')


'''
제출 답 
1. 14.3
def solution(scoville, K):
    scoville = sorted(scoville)
    answer = 0
    fail = []
    for i in range(1,K):
        fail.append(i)
    # print(len(scoville))
    while len(scoville) > 2 :
        # scovile 안에 스코빌 지수 아래의 수가 있는지 확인
        gap = list(set(fail) - set(scoville))
        if len(gap) == len(fail):
            break
        # cal 이라는 곳에 scovile 에 있는 가장 작은 수를 받아서 연산 후 다시 scovile에 넣어준다.
        cal = []
        cal.append(scoville.pop(0))
        cal.append(scoville.pop(0))
        result = cal[0] + cal[1] * 2
        scoville.append(result)
        scoville = sorted(scoville)
        print(scoville,'sco')
        answer += 1
        print(gap,'gap')

    return answer
    
    
2. 19.0


def solution(scoville, K):
    scoville = sorted(scoville)
    answer = 0
    fail = []
    for i in range(1,K+1):
        fail.append(i)
    print(fail,'fail')
    a = 0
    while True :
        if a >1000000:
            break
        a += 1
        # scovile 안에 스코빌 지수 아래의 수가 있는지 확인
        gap = list(set(fail) - set(scoville))
        if len(gap) == len(fail):
            break
        # cal 이라는 곳에 scovile 에 있는 가장 작은 수를 받아서 연산 후 다시 scovile에 넣어준다.
        cal = []
        cal.append(scoville.pop(0))
        cal.append(scoville.pop(0))
        result = cal[0] + cal[1] * 2
        scoville.append(result)
        scoville = sorted(scoville)
        print(scoville,'sco',a,'a')
        # print(gap, 'gap')
        answer += 1



    return answer

3. 23.8

def solution(scoville, K):
    scoville = sorted(scoville)
    answer = 0
    fail = []
    for i in range(1,K):
        fail.append(i)
    print(fail,'fail')
    a = 0
    while True :
        if a >1000000:
            break
        a += 1
        # 스코빌 지수를 K이상으로 만들 수 없는 경우 
        if len(scoville) == 1:
            if K+1 in scoville:
                pass
            else:
                return -1

        # scovile 안에 스코빌 지수 아래의 수가 있는지 확인
        gap = list(set(fail) - set(scoville))
        print(gap,'1st_gap')
        if len(gap) == len(fail):
            break
        # cal 이라는 곳에 scovile 에 있는 가장 작은 수를 받아서 연산 후 다시 scovile에 넣어준다.
        cal = []
        cal.append(scoville.pop(0))
        cal.append(scoville.pop(0))
        result = cal[0] + cal[1] * 2
        scoville.append(result)
        scoville = sorted(scoville)
        print(scoville,'sco',a,'a')
        # print(gap, 'gap')
        answer += 1




    return answer
'''