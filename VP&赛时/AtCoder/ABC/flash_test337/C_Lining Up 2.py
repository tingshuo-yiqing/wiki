"""
题意: N个人排队，给定数组A，A_i = -1表示第i人站在最前面，否则站在第A_i人正后方。输出从前到后的编号。
思路: 先找到排头（A_i = -1的人），用nxt数组记录每个人后面的人，从排头开始依次输出。
"""
def solve() -> None:
    N = int(input())
    A = list(map(int, input().split()))
    nxt = [0] * (N + 1)  # nxt[i] = i后面的人
    head = -1
    for i, a in enumerate(A, start=1):
        if a == -1:
            head = i
        else:
            nxt[a] = i
    cur = head
    ans = []
    for _ in range(N):
        ans.append(str(cur))
        cur = nxt[cur]
    print(" ".join(ans))

if __name__ == "__main__":
    solve()