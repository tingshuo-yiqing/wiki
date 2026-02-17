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
    outs = []
    for _ in range(II()):
        l, r = MII()

        f = False
        # ans = int(str(r)[::-1]) 
        # for i in range(r, l-1, -1):
        #     if i % 10 == 9:
        #         f = True
        #         outs.append(Max(ans, int(str(i)[::-1])))
        #         break
        ans = int(str(r))
        s = list(map(int, str(r)))[::-1]      
        j = 1
        while j < len(s) and s[j] == 0:
            j += 1
        if j < len(s):
            s[j] -= 1
        for k in range(j): 
            s[k] = 9
        num = int(''.join(map(str, s)))

        ans = Max(ans, num)
        outs.append(ans)

    print(*outs, sep='\n')

if __name__ == "__main__":
    main()