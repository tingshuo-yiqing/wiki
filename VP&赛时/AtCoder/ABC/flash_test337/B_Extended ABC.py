"""
题意: 判断字符串S是否由若干连续的A、之后连续的B、之后连续的C组成（每段可为空）。
思路: 遍历字符串，记录已出现的最大字母。若当前字符小于记录的最大字母，说明顺序错误，返回No；否则更新最大字母。最后输出Yes。
"""
def solve() -> None:
    S = input().strip()
    cur = 'A'  # 当前出现过的最大字母
    for ch in S:
        if ch < cur:
            print("No")
            return
        # 更新已出现的最大字母
        if ch > cur:
            cur = ch
    print("Yes")

if __name__ == "__main__":
    solve()