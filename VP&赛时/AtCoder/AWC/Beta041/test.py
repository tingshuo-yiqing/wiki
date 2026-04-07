from bisect import bisect_left, bisect


arr = [1, 2, 4, 5, 5, 5, 5, 7, 10]

r = bisect(arr, 3)  # 返回第一个大于target的数的下标

print(r)

l = bisect_left(arr, 3)  # 返回第一个大于等于target的数的下标

print(l)


