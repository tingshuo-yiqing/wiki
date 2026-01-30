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
        if ans == 0:
            outs.append((n + 2) // 3)
            continue

        L = s.find('1')
        R = s.rfind('1')

        l = 0
        while l < len(s):
            if s[l] == '0':
                r = l
                while r < len(s) and s[r] == s[l]:
                    r += 1
                is_left = l < L
                is_right = r > R
                if is_left or is_right:
                    ans += (r - l + 1) // 3
                else:
                    ans += (r - l) // 3
                l = r
            else:
                l += 1
        
        outs.append(ans)
    
    print(*outs, sep='\n')

if __name__ == "__main__":
    main()