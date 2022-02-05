'''
짝수와 홀수
https://programmers.co.kr/learn/courses/30/lessons/12937
문제 설명
정수 num이 짝수일 경우 "Even"을 반환하고 홀수인 경우 "Odd"를 반환하는 함수, solution을 완성해주세요.

제한 조건
num은 int 범위의 정수입니다.
0은 짝수입니다.

입출력 예
num	return
3	"Odd"
4	"Even"
'''
num = 3


def solution(num):
    answer = ''
    if num % 2 == 1:
        answer += "Odd"
    else:
        answer += "Even"
    return answer

print(solution(num))

'''
정리 : 비트화 등 몇몇 방법이 있는데, 내가 할 수 있던 것은 
case #3번과 같이 한줄로 썼으면 더 좋았을 것 같다. 

다른 사람의 답

case #1
def evenOrOdd(num):
    if (num%2):
        return "Odd"
    else:
        return "Even"

#아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : " + evenOrOdd(3))
print("결과 : " + evenOrOdd(2))

-> true , false 로 구분 /
 num % 2가 거짓(0)이라면 num % 2 ==0 (거짓) and Odd 가 되므로, 둘 다 참이어야하는 조건에 맞지 않기 때문에 or Even으로 해서 둘 중에 하나라도 참일 때 가능한 Even이 출력되며 , 
 num%2가 1(참)이면 and 조건이 성립되어 Odd가 출력됩니다
 
case #2
def evenOrOdd(num):
    return ["Even", "Odd"][num & 1]

#아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : " + evenOrOdd(3))
print("결과 : " + evenOrOdd(2))

-> & 연산자 비트 연산한 후  ["Even", "Odd"] 배열의 인덱스 처리

case #3
def evenOrOdd(num):
    return "Even" if num%2 == 0 else "Odd"

->return 에 if
'''
