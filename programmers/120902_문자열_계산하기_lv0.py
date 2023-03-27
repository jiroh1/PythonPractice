"""
문자열 계산하기
https://school.programmers.co.kr/learn/courses/30/lessons/120902
"""

def solution(my_string):
    answer = 0
    return answer

"""
다른풀이
# case1)
def solution(my_string):
    return eval(my_string)
or

solution=eval

# case 2)
def solution(my_string):
    s = my_string.split()
    answer = int(s[0])
    for i in range(1,len(s),2):
        if s[i]=='+':
            answer+=int(s[i+1])
        else:
            answer-=int(s[i+1])
    return answer
"""

"""
첫번째 시도
def solution(my_string):
    my_string=my_string.split(" ")
    answer=int(my_string[0])
    for i in my_string[1:]:
        try:
            temp=int(i)
        except:
            if i == '+':
                answer+=temp
            elif i == '-':
                answer-=temp
    return answer
"""
"""
정리
1. split 으로 나누어서 숫자인지 아닌지로 try문으로 나누어 진행하려고 했으나 실패
2. 그래서 결국 못풀고 케이스 찾아봤더니  case 2와 같이 풀 수 있었다.
3. 확인하는 것은 연산자만 확인하고, 나머지는 그뒤에꺼로 숫자를 더하는 방법
4. 3번을 생각해냈다면, 마지막 남은 숫자에 대한 고민을 해결할 수 있었다고 생각한다.
    -> range 에서 3번째 인자로 구별하는 것을 기억해야할 것이다.
5. case 1이 내장함수이다.
    5-1. string으로 와도 연산 가능하도록.
"""