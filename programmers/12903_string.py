'''
가운데 글자 가져오기
https://programmers.co.kr/learn/courses/30/lessons/12903
문제 설명
단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.

재한사항
s는 길이가 1 이상, 100이하인 스트링입니다.
입출력 예
s	return
"abcde"	"c"
"qwer"	"we"

'''
'''
# 첫시도 , 채점 시 오류가 계속 발생함. 
아무래도 round 때문인 것 같음.
s = "abcde"
# s = "qwer"
print(len(s))
def solution(s):
    answer=''
    # s의 글자 개수가 홀수 일 경우
    ls = int(len(s))
    a = round(ls / 2)
    #print(a, 'a')
    if ls % 2 == 1: answer = s[a]
    # s의 글자 개수가 짝수 일 경우
    elif ls % 2 == 0 : answer = s[a-1:a+1]
    return answer

print(solution("abcde"))
# print(solution("qwer"))
'''
# s = "abcde"
s = "qwer"
# b = (len(s)-1)//2
# print(b)
def solution(s):
    answer=''
    # s의 글자 개수가 홀수 일 경우
    if int(len(s)) % 2 == 1: answer = s[int(len(s)/2)]
    # s의 글자 개수가 짝수 일 경우
    elif int(len(s)) % 2 == 0 : answer = s[int(len(s)/2)-1:int(len(s)/2)+1]
    return answer
# print(solution("abcde"))
print(solution("powerk"))


'''
정리 : 몫을 구하면 되는 문제였는데, 굳이 if 문 없이도 몫만 구해서 아래와 같이 쉽게 구할 수 있었음. 
round에 집착하지 않았어도 됫었음

다른사람 답
def string_middle(str):
    # 함수를 완성하세요
    return str[(len(str)-1)//2:len(str)//2+1]
# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(string_middle("power"))

****** '//' :몫을 구하면 정수화 시켜주지 않아도 나누기 연산 후 소수점 이하의 수를 버리고, 정수 부분의 수만 구함
cf '%' : 몫이 아닌 나머지를 구함
'/' : 나누
================

def string_middle(str):
    a = len(str)
    if a % 2 == 0 :
        a = (a-2) / 2
    else :
        a = (a-1) / 2
    return str[int(a) : -int(a)]
# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(string_middle("power"))


'''