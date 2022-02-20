'''
lambda
https://dojang.io/mod/page/view.php?id=2359





'''
# def plus_ten(x):
#     return x + 10
#
# print(plus_ten(1))
# #11
#
# a = lambda x: x+10
# print(a)
# print(a(1))


# for step 1-3.py
def solution(num):
    print(num,type(num),type(num[0]),'1')
    num = list(map(str, num))
    print(num,type(num),type(num[0]),'2')
    num.sort(key=lambda x: x*2, reverse=True)
    print(num,type(num),type(num[0]),'3')
    return str(int(''.join(num)))


print(solution([3, 30, 34, 5, 9]))#9534330
'''
[3, 30, 34, 5, 9] <class 'list'> <class 'int'> 1
['3', '30', '34', '5', '9'] <class 'list'> <class 'str'> 2
['9', '5', '34', '3', '30'] <class 'list'> <class 'str'> 3
'''
#print(solution([6, 10, 2]))
'''
[6, 10, 2] <class 'list'> <class 'int'> 1
['6', '10', '2'] <class 'list'> <class 'str'> 2
['6', '2', '10'] <class 'list'> <class 'str'> 3
'''
num = ['330', '3', '31', '331']
num.sort(key=lambda x:x*3,reverse=True)
# *1['331', '330', '31', '3']
# *2 ['331', '330', '3', '31']
# *3 ['3', '331', '330', '31']
print(num, 'a')
if '30'<'3':
    print(True)
else :
    print(False)


'''
def solution(n):
    return int(''.join(sorted(str(int(n)), reverse=True)))
print(solution(118372))
'''