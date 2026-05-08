"""
题意: 高桥队和青木队进行了N场比赛，每场高桥得Xi分，青木得Yi分。总分多者胜，平局输出Draw。
思路: 分别累加两队总分，比较后输出对应结果。
"""
def solve() -> None:
    N = int(input())
    total_t, total_a = 0, 0
    for _ in range(N):
        x, y = map(int, input().split())
        total_t += x
        total_a += y
    if total_t > total_a:
        print("Takahashi")
    elif total_t < total_a:
        print("Aoki")
    else:
        print("Draw")

if __name__ == "__main__":
    solve()