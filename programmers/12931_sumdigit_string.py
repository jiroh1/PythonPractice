'''
자릿수 더하기
https://programmers.co.kr/learn/courses/30/lessons/12931

문제 설명
자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.
예를들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.

제한사항
N의 범위 : 100,000,000 이하의 자연수

입출력 예
N	answer
123	6
987	24

입출력 예 설명
입출력 예 #1
문제의 예시와 같습니다.

입출력 예 #2
9 + 8 + 7 = 24이므로 24를 return 하면 됩니다.''

'''

def solution(n):
    answer = 0
    n = str(n)
    for i in range(len(n)):
        # print(i,'i')
        # print(n[0][i],type(n[0][i]),i,'n')
#        print(n[i],type(n[i]),i,'n')
        answer += int(n[i])
    return answer

print(solution(9876))

'''
정리 : case#2와 같이 풀려고했으나 한줄로 안됬음. 중간에 단순 형변환만 하려고했는데, 나오는 값이 좀달라서 잠깐 헷갈렷음
숫자로 된 것이니, case #1과 같은 것도 알고 있으면 좋을 것 같고, 
case#3은 map 함수 이용하고 싶어했으니 그대로 하면 될 듯.
case#1 의 function 더 정확히 이해하기 
다른 답 :
case #1
def sum_digit(number):
    if number < 10:
        return number;
    return (number % 10) + sum_digit(number // 10) 
# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(sum_digit(123)));

case #2
def sum_digit(number):
    return sum([int(i) for i in str(number)])
# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(sum_digit(123)));

case#3
def sum_digit(number):
    return sum(map(int,str(number)))

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(sum_digit(123)));

 
'''