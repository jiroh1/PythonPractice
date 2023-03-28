"""
이진수더하기
https://school.programmers.co.kr/learn/courses/30/lessons/120885
"""
def solution(bin1, bin2):
    return bin(int(bin1,2) + int(bin2,2))[2:]
"""
정리
1. 이진수의 원리를 파이썬 기본 기능 없이 풀려고 했으나, 시간 낭비 같아서 안함
2. 기본 로직은 각 자리 수를 더해서 2가 되면 0으로 append 하고 앞 인덱스에 +1 더해주는 식으로
    list를 이용해서 풀려고했음
3. 노션에다가 정리는 해놨지만, int(input number, 원하는 진수)로 진수 변경 가능
4. [2:]는 진수 변경으로 생기는 문자열을 제거
"""