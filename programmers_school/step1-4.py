'''
Step1-4. 문제 먼저 직접 풀어보기 "큰 수 만들기"

프로그래밍1
- / 100.0
문제 설명
어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하려 합니다.

예를 들어, 숫자 1924에서 수 두 개를 제거하면 [19, 12, 14, 92, 94, 24] 를 만들 수 있습니다. 이 중 가장 큰 숫자는 94 입니다.

문자열 형식으로 숫자 number와 제거할 수의 개수 k가 solution 함수의 매개변수로 주어집니다.
number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자를 문자열 형태로 return 하도록 solution 함수를 완성하세요.

제한 조건
number는 1자리 이상, 1,000,000자리 이하인 숫자입니다.
k는 1 이상 number의 자릿수 미만인 자연수입니다.

입출력 예
number	k	return
"1924"	2	"94"
"1231234"	3	"3234"
"4177252841"	4	"775841"

'''
# 1<len(number)<1,000,000
# 1< k < len(str(number)
from itertools import permutations

def solution(number, k):
    answer = ''
    num = list(str(number))
    # print(number,type(number),'number')
    print(num,type(num),'num')
    j=0
    for i in range(len(num)):
        # print(len(num),'이거')
        if i ==0:
            pass
        if num[i-1]<num[i]:
            num.pop(i-1)
            print(num[i],'2번')
            j+=1

        else:
            print('다시')
            continue

        print(num,j,'j')
    # answer=''.join(num)
    return answer

# def solution(number, k):
#     answer = ''
#     num = list(str(number))
#     # print(number,type(number),'number')
#     ans = list(permutations(num,(len(num)-2)))
#     print(ans)
#     for i in range(len(ans)):
#        ans[i] = list(ans[i])
#        print(ans[i],'p',type(ans[i]),ans[i][0],type(ans[i][0]) , 'check')
#     a=''.join(ans[i])
#     print(a,type(a))
#     return answer
#print(solution(1924,2))
print(solution(1231234,3)) #"3234"
'''
자릿수 구하기 : https://shoark7.github.io/programming/algorithm/3-ways-to-get-length-of-natural-number
한글자 씩 나누기: https://bio-info.tistory.com/29
'''