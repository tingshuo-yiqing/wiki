import sys
from collections import Counter
from math import inf
if 1:
    inp = lambda: sys.stdin.readline().strip()

    II = lambda: int(inp())
    MII = lambda: map(int, inp().split())
    LII = lambda: list(MII())

    Max = lambda x, y: x if x > y else y
    Min = lambda x, y: x if x < y else y

def main():
    n, m = MII()
    a = LII()

    k = n // m  # 让 [0, m-1] 都出现 k 次

    rem = []
    for x in a:
        rem.append(x % m)
    
    ans = 0
    st = []
    cnt = Counter(rem)

    # for _ in range(2):
    #     for r in range(m):


    print(ans)


if __name__ == "__main__":
    main()