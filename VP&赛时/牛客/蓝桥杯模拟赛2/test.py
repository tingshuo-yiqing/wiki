from collections import deque


dq = deque([1, 2,3 ,4 ,5])

print(*dq)

dq.rotate(-1)
print(*dq)

dq.rotate(1)
print(*dq)


print(0 % 4)

print(263 / 1030)