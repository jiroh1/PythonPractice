def solution(number, k):
    stack = []
    for i in number:
        while k > 0 and stack:
            if stack[-1] < i:
                stack.pop()
                k -= 1
            else:
                break
        stack.append(i)
    answer = ''.join(stack)
    return answer

#print(solution(1924,2))
print(solution(1231234,3)) #"3234"