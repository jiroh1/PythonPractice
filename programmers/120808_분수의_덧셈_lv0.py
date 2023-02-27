"""
분수의 덧셈
https://school.programmers.co.kr/learn/courses/30/lessons/120808
"""
import math
def solution(numer1, denom1, numer2, denom2):
    bmo= denom1*denom2
    bja=denom1*numer2+denom2*numer1
    
    gcd_value=math.gcd(bmo,bja)
    print(gcd_value)
    answer=[bja/gcd_value,bmo/gcd_value]

    return answer

numer1,	denom1,	numer2,	denom2 = 1,	2	,3	,4

print(solution(numer1,	denom1,	numer2,	denom2))
# if __name__=="__main__":
#     solution(numer1,	denom1,	numer2,	denom2)

"""
문제 설명
첫 번째 분수의 분자와 분모를 뜻하는 numer1, denom1, 두 번째 분수의 분자와 분모를 뜻하는 numer2, denom2가 매개변수로 주어집니다. 
두 분수를 더한 값을 기약 분수로 나타냈을 때 분자와 분모를 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.

제한사항
0 <numer1, denom1, numer2, denom2 < 1,000
입출력 예
numer1	denom1	numer2	denom2	result
1	2	3	4	[5, 4]
9	2	1	3	[29, 6]
입출력 예 설명
입출력 예 #1

1 / 2 + 3 / 4 = 5 / 4입니다. 따라서 [5, 4]를 return 합니다.
입출력 예 #2

9 / 2 + 1 / 3 = 29 / 6입니다. 따라서 [29, 6]을 return 합니다.
"""
"""
다른 풀이
# case 1
from fractions import Fraction

def solution(denum1, num1, denum2, num2):
    answer = Fraction(denum1, num1) + Fraction(denum2, num2)
    return [answer.numerator, answer.denominator]

# case 2
"""