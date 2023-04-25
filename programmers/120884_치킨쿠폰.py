"""
치킨쿠폰
https://school.programmers.co.kr/learn/courses/30/lessons/120884
"""

def solution(chicken):
    all=0
    while chicken >= 10:
        a,b=divmod(chicken,10)
        all += a
        chicken = a+b
        
    return all


"""
정리
1. while문법 할 때마다 뭔가 어색해서 남김.
2. while과 divmod 헷갈린 것에 대해서 잘 적용한듯.

"""