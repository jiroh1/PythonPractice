from itertools import combinations
def solution(number):
    answer = 0
    com = list(combinations(number,3))
    return len([answer for c in com if sum(c) ==0])
