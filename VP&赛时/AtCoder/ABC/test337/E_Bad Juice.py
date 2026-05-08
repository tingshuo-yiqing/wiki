# ABC337E - Bad Juice
# 题意：交互题。N 瓶果汁中恰好有 1 瓶变质。需要召集最少的朋友，让每位朋友
#       品尝若干瓶果汁。第二天根据朋友是否不舒服来判断哪瓶变质。
#       要求输出最小朋友数以及每位朋友喝的果汁，最后推断变质果汁编号。
# 思路：M 个朋友的信息（0/1）可以区分 2^M 种情况，因此最小 M = ceil(log2(N))。
#       将果汁编号 1~N 看作二进制，第 i 位朋友喝所有二进制第 i 位为 1 的果汁。
#       收到反馈后，不舒服的朋友对应位为 1，合成二进制数即变质果汁编号。
#       注意：如果编号全 0 对应 N=2^M 时的第 N 瓶，需要特殊处理。

import sys
import math

def solve():
    N = int(input())
    M = math.ceil(math.log2(N))  # 最小朋友数
    print(M, flush=True)

    # 为每位朋友准备要喝的果汁列表
    friends = [[] for _ in range(M)]
    for juice in range(1, N + 1):
        # 将 juice 的二进制位分配给对应的朋友
        for bit in range(M):
            if (juice >> bit) & 1:
                friends[bit].append(juice)

    # 输出每位朋友喝的果汁
    for i in range(M):
        print(len(friends[i]), *friends[i], flush=True)

    # 接收每位朋友是否不舒服的反馈
    S = input().strip()

    # 根据反馈确定变质果汁
    ans = 0
    for i, ch in enumerate(S):
        if ch == '1':
            ans |= (1 << i)

    # 如果 ans == 0 或 ans > N，说明是编号为 N 的那瓶（最高位全 0 的情况）
    if ans == 0 or ans > N:
        ans = N

    print(ans, flush=True)

if __name__ == "__main__":
    solve()