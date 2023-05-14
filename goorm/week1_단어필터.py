# 문자열 구현 문제

# 제출 답안

import sys

input=sys.stdin.readline
word_length, message_length = map(int,input().split())
word = input().rstrip()
message = input().rstrip()

while word in message:
	message=message.replace(word, '')

if message:
	print(message)
elif len(message) == 0:
	print('EMPTY')
	
"""
정리
중간에 while 문 대신 if 문으로 했는데, '문제에서 메시지 E에 더 이상 단어 S가 존재하지 않을 때까지 반복해서 필터링을 적용한다.' 이 부분을 적용 하기엔
if문은 안되고, while문이 되는 것이다.
->문제를 좀 놓치는 부분을 줄여야 한다. 조급해하지말고.
"""
"""
추가 풀이

들여쓰기가 되어있지 않아 잘은 모르겠습니다만, 결과 출력부분에서 문제가 생길수 있을것같습니다.

질문하신 코드가 아래의 코드가 맞다면, 아래의 코드를 기준으로 말씀드리겠습니다.

import sys

input = sys.stdin.readline
word_length, message_length = map(int,input().split())
word = input().rstrip()
message = input().rstrip()

# while을 if로 바꿨을 경우
if word in message: 
    message = message.replace(word, '')

if message:
    print(message)
else:
    print('EMPTY')
while을 if로 바꿨을 경우, if word in message는 message를 인덱스의 처음부터 끝까지 1번만 순회합니다.

예를 들어

입력 :

2 7

ab

aababba

의 경우에 if문의 word는 a ab ab ba를 탐색하고 ab ab를 ''로 치환한 뒤, aba를 message에 저장합니다.

정답 :

a

제시한 코드의 출력결과 :

aba

while은 word가 message안에 없을때까지 순회하며 message 내의 word를 ''로 치환합니다.

while문 내에서의 message 저장값은 다음과 같습니다.

1회 : aababba

2회 : aba

3회 : a

최종적으로 message = 'a' 가 저장됩니다.

import sys

input = sys.stdin.readline
word_length, message_length = map(int,input().split())
word = input().rstrip()
message = input().rstrip()

while word in message:
    message = message.replace(word, '')

if message:
    print(message)
else:
    print('EMPTY')
"""