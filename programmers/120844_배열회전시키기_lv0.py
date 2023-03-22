"""
배열 회전시키기
https://school.programmers.co.kr/learn/courses/30/lessons/120844
"""

# 제출답안
from collections import deque
def solution(numbers, direction):
    if direction=='right':
        deq=deque(numbers)
        deq.appendleft(numbers[-1])
        numbers=list(deq)[:-1]        
    else:
        numbers.append(numbers[0])
        numbers.remove(numbers[0])
    return numbers
"""
다른풀이
# case1)
def solution(numbers, direction):
    return [numbers[-1]] + numbers[:-1] if direction == 'right' else numbers[1:] + [numbers[0]]

# case2)
from collections import deque

def solution(numbers, direction):
    numbers = deque(numbers)
    if direction == 'right':
        numbers.rotate(1)
    else:
        numbers.rotate(-1)
    return list(numbers)    
"""

"""
정리
왼쪽 앞에 넣어야 하는 생각 때문에 
deque의 appendleft 를 써야 겠다는 생각을 했음.
left 에 대해서는 그냥 맨앞에꺼넣고 맨앞에꺼 빼면 된다고 생각했음
정리를 남기는 이유는 다른 답안을 공부하기 위함.

case 1 처럼 슬라이싱을 끝내는 것이 제일 좋았을 것 같다.
그리고 deque 를 쓰려고 했으면 case 2 처럼 rotate()를 썼어야했다.
notion에 정리한 deque에 대해서 다시 한번 확인 해보면 좋을 듯 
"""
