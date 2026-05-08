"""
题意: N瓶果汁中恰好1瓶变质，可让M位朋友品尝任意组合，第二天知道谁肚子不舒服（对应二进制位为1），需用最少朋友数确定变质果汁编号。
思路: 最少朋友数M = ceil(log2(N))，每位朋友对应一个二进制位，喝其位为1的果汁。根据反馈的二进制串即可确定变质果汁编号（需注意编号从1开始，二进制大小+1）。
"""
import sys

def solve() -> None:
    N = int(sys.stdin.readline())
    # 求最少朋友数 M = ceil(log2(N))
    M = (N - 1).bit_length()  # ceil(log2(N))

    # 输出朋友数
    print(M, flush=True)

    # 对每位朋友，输出他喝的果汁编号（第i位二进制为1的编号，使用0-based索引）
    for i in range(M):
        drink = []
        for juice in range(1, N + 1):
            if (juice - 1) >> i & 1:
                drink.append(juice)
        print(len(drink), *drink, flush=True)

    # 读取反馈结果
    S = sys.stdin.readline().strip()
    # 将二进制串转为整数（0-based索引）
    ans = 0
    for i, ch in enumerate(S):
        if ch == '1':
            ans |= 1 << i
    # 转为1-based编号
    print(ans + 1, flush=True)

if __name__ == "__main__":
    solve()