# ABC337C - Lining Up 2
# 题意：N个人排队，给定信息 A_i：若 A_i = -1 则第 i 个人在最前面，
#       否则第 i 个人在第 A_i 个人正后方。输出从前到后的排队顺序。
# 思路：找到 A_i = -1 的人作为起点，然后根据"谁在谁后面"的关系链式查找。
#       用数组 nxt 记录每个人的后一个人，从起点开始依次输出即可。

N = int(input())
A = list(map(int, input().split()))

nxt = [0] * (N + 1)  # nxt[i] 表示第 i 个人后面的那个人
start = 0

for i, a in enumerate(A, 1):
    if a == -1:
        start = i
    else:
        nxt[a] = i

ans = []
cur = start
for _ in range(N):
    ans.append(str(cur))
    cur = nxt[cur]

print(" ".join(ans))