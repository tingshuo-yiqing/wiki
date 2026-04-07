import sys

Max = lambda x, y: x if x > y else y
Min = lambda x, y: x if x < y else y

input_type = 1

if input_type:
    inp = lambda: sys.stdin.readline().strip()

    II = lambda: int(inp())
    MII = lambda: map(int, inp().split())
    LII = lambda: list(MII())


def main():
    n, t, k = MII()

    a = sorted(LII())

    d = a[0] - 1

    ans = sum(1 for x in a if t + k >= x - d)
    print(ans)

if __name__ == "__main__":
    main()
