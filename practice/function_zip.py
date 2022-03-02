'''
a = list(zip([1, 2, 3], [4, 5, 6]))
#[(1, 4), (2, 5), (3, 6)]
b = list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9]))
#[(1, 4, 7), (2, 5, 8), (3, 6, 9)]
c = list(zip("abc", "def"))
#[('a', 'd'), ('b', 'e'), ('c', 'f')]
#print(a)
'''
arr1 = [[1,2],[2,3]]
arr2 = [[3,4],[5,6]]

# for a, b in zip(arr1,arr2):
#     c, d = a+b
#     print(c,d,'ab')
#     for c,d in zip(c,d):
#         ans = [c+d]
#     print(ans)


def sumMatrix(A,B):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]
    # answer = [a + b for a, b in zip(A, B)]
    return answer

print(sumMatrix(arr1,arr2))
