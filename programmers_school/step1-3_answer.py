def solution(numbers):
    numbers = [str(x) for x in numbers]
    numbers.sort(key=lambda x : (x * 4)[:4], reverse=True)
    if numbers[0] == '0':
        answer = '0'
    else:
        answer = ''.join(numbers)
    return answer

print(f'순서를 재배치하여 만들 수 있는 가장 큰 수는 : {solution([3, 30, 34, 5, 9])}')

'''
정렬을 하고 문제를 푸는 것이 최적의 방법
'''