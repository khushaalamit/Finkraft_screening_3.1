# Write a Python program that finds the longest common substring between two strings

first_string = input('Enter First String: ')
second_string = input('Enter Second String: ')


def sub_st(st1, st2):
    start = (i for i, (a, b) in enumerate(zip(st1, st2)) if a != b)
    common_len = next(start, min(len(st1), len(st2)))
    return st1[:common_len]


sub1 = dict()
for i, c in enumerate(first_string):
    sub1.setdefault(c, []).append(i)
max_string = max((sub_st(second_string[i:], first_string[j:]) for i, c in enumerate(
    second_string) for j in sub1.get(c, [])), key=len)
print('the longest common substring between two strings is: ', max_string)
