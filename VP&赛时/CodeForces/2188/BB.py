import sys
from math import inf

inp = lambda: sys.stdin.readline().strip()

II = lambda: int(inp())
MII = lambda: map(int, inp().split())
LII = lambda: list(MII())

Max = lambda x, y: x if x > y else y
Min = lambda x, y: x if x < y else y

def main():
    outs = []
    for _ in range(II()):
        n = II()
        s = inp()

        ans = s.count('1')

        s  = '1' + s + '1'  # 确保'0'前一定有一个'1'
        l = 0
        for i in range(len(s)):
            if s[i] == '0':
                if s[i - 1] == '1':
                    l = i
                if s[i + 1] == '1':
                    # 当'1'是在最左边后最右边时要加上，真正中间的才是减2
                    t = (l == 1) + (i == n)
                    ans += (i - l + 1 + t) // 3
        
        outs.append(ans)
    print(*outs, sep='\n')

if __name__ == "__main__":
    main()