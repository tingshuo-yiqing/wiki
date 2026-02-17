import sys
from math import inf
if 1:
    inp = lambda: sys.stdin.readline().strip()

    II = lambda: int(inp())
    MII = lambda: map(int, inp().split())
    LII = lambda: list(MII())

    Max = lambda x, y: x if x > y else y
    Min = lambda x, y: x if x < y else y

def main():
    n = II()
    s = inp()

    cnt = 0

    for i, c in enumerate(s):
        cnt += 1 if c == '(' else -1

    if abs(cnt) != 2:
        print(0)
        sys.exit(0)

    pf = [0] * (n + 1)  # 记录前 [0, i-1] 括号序列的信息
    pfok = [True] * (n + 1)
    for i in range(n):
        pf[i + 1] = pf[i] + (1 if s[i] == '(' else -1)
        pfok[i + 1] = pfok[i] & (pf[i + 1] >= 0)
    
    sf = [0] * (n + 1)  # 记录 [i, n] 括号序列的信息
    sfok = [True] * (n + 1)
    for i in range(n-1, -1, -1):
        sf[i] = sf[i + 1] + (1 if s[i] == ')' else -1)
        sfok[i] = sfok[i + 1] & (sf[i] >= 0)
    
    ans = 0
    for i in range(n):
        if not pfok[i] or not sfok[i + 1]:
            continue
        if s[i] == '(':
            if pf[i] > 0 and pf[i] - 1 == sf[i + 1]: # 被删除的位置应该是 pf[i]+1 删完后就是 pf[i]+1-2了
                ans += 1
        else:
            if pf[i] + 1 == sf[i + 1]:
                ans += 1

    print(ans) 

if __name__ == "__main__":
    main()