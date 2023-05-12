# 문자열 구현 문제
"""
대문자는 소문자로 소문자는 대문자로 변경하는 문제
쉬운 문제지만 sys.stdin.readline 의 사용방법 때문에 작성
input()의 특징
1. 입력 받은 문자열을 문자 단위로 읽는다.
2. 개행 문자를 삭제한다.
3. 문자를 문자열로 변환하여 반환한다.
즉, 입력 받은 문자열을 문자 단위로 하나씩 읽어들이기 때문에 느리다.
수십만 건의 입력을 받아야 한다면 timeout이 뜨는 경우도 종종 마주할 것이다.

그래서 사용자의 입력을 받는 버퍼를 만든 뒤, 그 버퍼에서 입력을 다시 읽어 들이는 sys.stdin.readline() 함수를 이용 하는 것이다.
(<built-in method readline of _io.TextIOWrapper object at 0x7fb3cbd83558> )

"""

# import sys
# input=sys.stdin.readline
# length = int(input())
# word_input = input().rstrip()

# answer=''
# for w in word_input:
# 	if w.islower():
# 		answer+=w.upper()
# 	elif w.isupper():
# 		answer+=w.lower()
# print(answer)

# # 내장함수 swapcase()로 풀이
# import sys
# input = sys.stdin.readline
# N = int(input())
# S = input().rstrip()
# # swapcase()는 문자열의 대문자를 소문자로, 소문자를 대문자로 치환해준다.
# print(S.swapcase())

import sys
input = sys.stdin.readline
N = int(input())
S = input().rstrip()

print(input,'/',N,S)

"""
예시
10
goormLevel
출력
GOORMlEVEL
"""