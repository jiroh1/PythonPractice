def solution(n):
    answer = []
    while n != 1:
        answer.append(n)
        if n % 2 == 0:
            n = n // 2
            if n == 2:
                answer.append(2)
                answer.append(1)
                return answer
        elif n % 2 == 1:
            n = 3 * n + 1

        continue
    