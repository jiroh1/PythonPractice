"""

K번째수
https://programmers.co.kr/learn/courses/30/lessons/42748

문제 설명
배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려 합니다.

예를 들어 array가 [1, 5, 2, 6, 3, 7, 4], i = 2, j = 5, k = 3이라면

array의 2번째부터 5번째까지 자르면 [5, 2, 6, 3]입니다.
1에서 나온 배열을 정렬하면 [2, 3, 5, 6]입니다.
2에서 나온 배열의 3번째 숫자는 5입니다.
배열 array, [i, j, k]를 원소로 가진 2차원 배열 commands가 매개변수로 주어질 때,
commands의 모든 원소에 대해 앞서 설명한 연산을 적용했을 때 나온 결과를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

제한사항
array의 길이는 1 이상 100 이하입니다.
array의 각 원소는 1 이상 100 이하입니다.
commands의 길이는 1 이상 50 이하입니다.
commands의 각 원소는 길이가 3입니다.

입출력 예
array               	commands	                        return
[1, 5, 2, 6, 3, 7, 4]	[[2, 5, 3], [4, 4, 1], [1, 7, 3]]	[5, 6, 3]

입출력 예 설명
[1, 5, 2, 6, 3, 7, 4]를 2번째부터 5번째까지 자른 후 정렬합니다. [2, 3, 5, 6]의 세 번째 숫자는 5입니다.
[1, 5, 2, 6, 3, 7, 4]를 4번째부터 4번째까지 자른 후 정렬합니다. [6]의 첫 번째 숫자는 6입니다.
[1, 5, 2, 6, 3, 7, 4]를 1번째부터 7번째까지 자릅니다. [1, 2, 3, 4, 5, 6, 7]의 세 번째 숫자는 3입니다.

"""

# 제출코드


def solution(array, commands):
    answer = []
    for num in commands:
        i = num[0]
        j = num[1]
        k = num[2]

        cut = array[i - 1:j]
        cut.sort()
        cut = cut[k - 1]
        answer.append(cut)

    return answer

def solution(array, commands):
    check = list(map(lambda x: sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
    print(check)
    return list(map(lambda x: sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

def solution(array, commands):
    return [sorted(array[a-1:b])[c-1] for a,b,c in commands]

# 새싹 강사님 답안
def solution(array, commands):
    answer = []

    for i,j,k in commands:
        #1번째 연산 자르기 (i번째부터 j번째까지)
        new_array = array[i-1:j]
        #2번째연산 정렬하기
        new_array.sort()
        #3번째 연산 k번째 값 가져오기
        answer.append(new_array[k-1])

    return answer
print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))


'''
정리 : 
틀렸다기보단 잘풀었다고 생각한데 이걸 한줄에 그리고 lamda와 map을 써서 속도를 조금더 빠르게 해주는 버릇을 드리는 것이 좋을 것 같다.

다른풀이:
#case 01
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
    
    
#case 02
def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command
        answer.append(list(sorted(array[i-1:j]))[k-1])
    return answer
    
#case 03
def solution(array, commands):
    result = []
    for command in commands:
        i, j, k = command[0], command[1], command[2]
        subarray = sorted(array[i-1:j])
        result.append(subarray[k-1])
    return result
    
#case 04
def solution(array, commands):
    return [sorted(array[a-1:b])[c-1] for a,b,c in commands]
    
'''