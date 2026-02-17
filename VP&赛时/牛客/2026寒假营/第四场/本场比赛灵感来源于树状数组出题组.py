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

    a = LII()

    ans = []
    for i in range(n):
        cnt = 0
        for j in range(n):
            if i == j:
                continue
            if a[j] <= a[i]:
                cnt += 1
        if cnt * 5 >= (n - 1) * 4:
            ans.append(a[i])
    
    print(sum(ans))

if __name__ == "__main__":
    main()