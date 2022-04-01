"""
하샤드 수
https://programmers.co.kr/learn/courses/30/lessons/12947

문제 설명
양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다. 예를 들어 18의 자릿수 합은 1+8=9이고, 18은 9로 나누어 떨어지므로 18은 하샤드 수입니다.
자연수 x를 입력받아 x가 하샤드 수인지 아닌지 검사하는 함수, solution을 완성해주세요.

제한 조건
x는 1 이상, 10000 이하인 정수입니다.

입출력 예
arr	return
10	true
12	true
11	false
13	false

입출력 예 설명
입출력 예 #1
10의 모든 자릿수의 합은 1입니다. 10은 1로 나누어 떨어지므로 10은 하샤드 수입니다.

입출력 예 #2
12의 모든 자릿수의 합은 3입니다. 12는 3으로 나누어 떨어지므로 12는 하샤드 수입니다.

입출력 예 #3
11의 모든 자릿수의 합은 2입니다. 11은 2로 나누어 떨어지지 않으므로 11는 하샤드 수가 아닙니다.

입출력 예 #4
13의 모든 자릿수의 합은 4입니다. 13은 4로 나누어 떨어지지 않으므로 13은 하샤드 수가 아닙니다.

"""


def solution(x):
    x = str(x)
    answer = True
    mid = 0
    for i in range(len(x)):
        mid += int(x[i])
    print(int(x)//mid,'/',mid,'123')
    if int(x) % mid == 0:
        print('!')
        return answer
    else:
        return False

# 제출답안


def solution(x):
    x = str(x)
    answer = True
    mid = 0
    for i in range(len(x)):
        mid += int(x[i])
    if int(x) % mid == 0:
        return answer
    else:
        return False

# 최종제출


def solution(x):
    answer = True
    mid = 0
    for i in range(len(str(x))):
        mid += int(str(x)[i])
    if x % mid == 0:
        return answer
    else:
        return False

def solution(n):
    for c in str(n):
        print(c)

print(solution(11))

print(sum([1,2,3]))
# print(10 % 3)
# print(10//2)

"""
정리: 생각보다 어렵진 않았다.
단 아래처럼 for문의 범위를 쉽게 가져갈 수 있었는데, 어렵게 형변환 했다.
sum 함수를 사용하면 좋을 것 같다.
https://blockdmask.tistory.com/413

다른풀이 :

# case01
def Harshad(n):
    # n은 하샤드 수 인가요?
    return n % sum([int(c) for c in str(n)]) == 0

"""