# from math import factorial
# print(factorial(12))
# print(factorial(10))
# print(factorial(7))

# s = "ABCDEFGHI"
# k = 5
# n = len(s)
# print(n)
# for i in range(n - k + 1):
#     print(s[i:i + k])

arr = [1, 2, 3, 4, 5, 6, 7, 9, 100]

from bisect import bisect_left

print(bisect_left(arr, 3))  #! 返回 0-based

print(bisect_left(arr, 11))