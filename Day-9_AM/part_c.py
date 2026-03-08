# Q1 — Shallow vs Deep Copy

import copy

original = [[1,2],[3,4]]

shallow = copy.copy(original)
deep = copy.deepcopy(original)

original[0][0] = 99

print("Original:", original)
print("Shallow:", shallow)
print("Deep:", deep)


# Q2 — Rotate List

def rotate_list(lst, k):

    k = k % len(lst)

    return lst[-k:] + lst[:-k]


print(rotate_list([1,2,3,4,5],2))


# Q3 — Debug Problem

nums = [1,2,3,4,5,6,7,8]

correct = [n for n in nums if n % 2 != 0]

print(correct)