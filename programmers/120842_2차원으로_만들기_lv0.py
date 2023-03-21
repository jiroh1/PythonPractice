"""
2차원으로 만들기
https://school.programmers.co.kr/learn/courses/30/lessons/120842
"""

def solution(num_list, n):    
    return [num_list[i*n:(i+1)*n] for i in range(len(num_list)//n)]

num_list=[1, 2, 3, 4, 5, 6, 7, 8]		
n=2	# [[1, 2], [3, 4], [5, 6], [7, 8]]
# num_list=[100, 95, 2, 4, 5, 6, 18, 33, 948]
# n=3	# [[100, 95, 2], [4, 5, 6], [18, 33, 948]]

print(solution(num_list, n))

"""
정리 
처음 접근했던 range를 n으로 나누어서 하는 것이 맞았고,
그 요소를 slicing 해서 뽑아 내는 것만 구현 했으면 되었음.
"""