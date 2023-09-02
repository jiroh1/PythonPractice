def solution(a, d, included):
    answer = 0
    for i , x in enumerate(included):
        if x == True :
            answer += a + i * d
        else :
            pass
    return answer 
            