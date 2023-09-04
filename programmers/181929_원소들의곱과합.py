def solution(num_list):
    standard = sum(num_list)**2
    a = 1
    for i in num_list:
        a *= i
    if a < standard:
        return 1
    return 0
    