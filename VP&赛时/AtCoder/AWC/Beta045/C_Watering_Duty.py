import sys

Max = lambda x, y: x if x > y else y
Min = lambda x, y: x if x < y else y

inp = lambda: sys.stdin.readline().strip()

II = lambda: int(inp())
MII = lambda: map(int, inp().split())
LII = lambda: list(MII())


def main():
    n, q = MII()

    d = [0] * (n + 1)

    for _ in range(q):
        l, r, v = MII()

        d[l] += v
        if r + 1 <= n:
            d[r + 1] -= v

    cur = 0
    for i in range(1, n + 1):
        cur += d[i]
        print(cur, end=' ')
        

if __name__ == "__main__":
    main()
