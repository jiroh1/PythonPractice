def solution(my_strings, parts):
    return ''.join([s[i[0]:i[1]+1] for s, i in list(zip(my_strings,parts))])