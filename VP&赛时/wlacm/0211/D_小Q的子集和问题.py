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
    for _ in range(II()):
        n = II()
        a = LII()
        a.sort()

        f = False
        s1 = sum(a[:-1])
        for i in range(n + 1):
            if s1 - a[i] == a[-1]:
                ans = []
                for j in range(n + 1):
                    if i == j:
                        continue
                    ans.append(a[j])
                f = True
                print(*ans)         
                break  
            
        if not f:
            if sum(a[:-2]) == a[-2]:
                f = True
                print(*a[:-2])

        if not f:
            print(-1)

if __name__ == "__main__":
    main()