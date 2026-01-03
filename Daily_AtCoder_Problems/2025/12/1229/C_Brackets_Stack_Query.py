import sys
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def main():
    n = int(input())

    blance = 0
    min_blace = 0   # 追踪 ) 在 ( 前的情况，这种即使blace为0也是不平衡的

    st = [(blance, min_blace)]  # 初始状态
    outs = []

    for _ in range(n):
        o = input().split()

        if o[0] == '1':
            blance += 1 if o[1] == '(' else -1
            min_blace = min(min_blace, blance)

            st.append((blance, min_blace))
        else:
            # 去掉最末尾一个括号，即回到上一状态
            st.pop()

        blance, min_blace = st[-1]
        if min_blace == 0 and blance == 0:
            outs.append("Yes")
        else:
            outs.append("No")

    print(*outs, sep='\n')
if __name__ == "__main__":
    main()