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

    memo = {}
    for j in range(n):
        _ = II()
        a = LII()
        
        s = sum(a)
        for i, x in enumerate(a):
            t = s - x
            if t in memo and memo[t][0] != j + 1:
                print("YES")
                print(memo[t][0], memo[t][1])
                print(j + 1, i + 1)
                return
            memo[t] = (j + 1, i + 1)

    print("NO")

if __name__ == "__main__":
    main()