import sys

inp = lambda: sys.stdin.readline().strip()

II = lambda: int(inp())
MII = lambda: map(int, inp().split())
LII = lambda: list(MII())

Min = lambda x, y: x if x < y else y
Max = lambda x, y: x if x > y else y

def main():
    n, m = MII()
    a = LII()

    for x in a:
        m = m * x // 100

    print(m)


if __name__ == "__main__":
    main()
