'''
정수 내림차순으로 배치하기
https://programmers.co.kr/learn/courses/30/lessons/12933

문제 설명
함수 solution은 정수 n을 매개변수로 입력받습니다. n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요. 예를들어 n이 118372면 873211을 리턴하면 됩니다.

제한 조건
n은 1이상 8000000000 이하인 자연수입니다.
입출력 예
n	return
118372	873211

'''
# 답
def solution(n):
    return int(''.join(sorted(str(int(n)), reverse=True)))
print(solution(118372))

'''
풀지 못했던 풀이
n = [1,1,8,3,7,2]
# print(n[5], 'last')
# print(len(n))
#n='118372'
answer = []
for i in range(len(n)):
    print(i,'index')
    if n[i] > n[i-1]:
        answer.append(n[i])
        print(n,'n')
        print(answer,'answer')
    else:
        continue
'''


'''
정리: 1. 형타입에 대해서 명확히 하는 것이 좋다.
2. 하루 고민 해봤으나, for 문과 append로 풀려고 하다가 안됨.
->하루정도 지나서 풀이를 검색함 
3. string으로 생각하는 것은 맞았음. 
4.sorted 에서 reverse =True 로 바꾸면 내림차순으로 변한다.
5. ''.join을 해주면 요소들을 공백없이 하나의 문자열로 합쳐준다.( list 내 요소에서도 가능)
6 case #3과 같이 list에 append 하면서 넣을 순 있었을 것 같음.. 하지만 쉽지 않다.

다른풀이:

case #1
def solution(n):
    ls = list(str(n))
    ls.sort(reverse = True)
    return int("".join(ls))

case #2
def solution(n):
    num=list(str(n))
    num.sort(reverse=True)
    answer=" "
    for k in num:
        answer+=str(k)
    return int(answer)
    
case #3

def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] >= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
    return result

def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = mergeSort(left)
    right = mergeSort(right)

    return merge(left, right)

def solution(n):
    arr = list(str(n))
    n = int(''.join(mergeSort(arr)))
    return n
    
'''