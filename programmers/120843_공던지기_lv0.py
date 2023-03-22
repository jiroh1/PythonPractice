"""
공던지기
https://school.programmers.co.kr/learn/courses/30/lessons/120843
"""

# 최종 제출 답안
def solution(numbers, k):
    if len(numbers)%2==0:
        result=numbers[0::2]
    else:
        result=numbers[0::2]+numbers[1::2]
    return result[(k%len(result))-1]
    

# 처음 제출 답안
def solution(numbers, k):
    if len(numbers) % 2 ==0:
        return numbers[int(k//(len(numbers)/2))+1]
    elif len(numbers) % 2 !=0:
        temp=[]
        for i in range((len(numbers)//2)+1):
            temp.append(2*i+1)
        for i in range(1,len(numbers)//2+1):
            temp.append(2*i)
        return temp[int(k//(len(numbers)/2))+1]

"""
정리
처음, 길이가 짝수 인것은 홀수만 왔다 갔다 하는 것에 꽂혀서 좀 오래 걸렸다.
그 생각과 가장 비슷한 답안이 최종 제출 답안 
'슬라이싱'으로 구현하는 것을 배열에서는 잘 이용해야 할듯 
"""     
""" 
다른풀이
# case1
def solution(numbers, k):
    return numbers[2 * (k - 1) % len(numbers)]
# case2
def solution(numbers, k):
    return 2 * (k - 1) % numbers[-1] + 1

"""