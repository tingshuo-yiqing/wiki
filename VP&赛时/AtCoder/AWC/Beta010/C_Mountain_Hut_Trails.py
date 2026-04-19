import sys

Min = lambda x, y: x if x < y else y
Max = lambda x, y: x if x > y else y

inp = lambda:sys.stdin.readline().strip()

II = lambda: int(inp())
MII = lambda: map(int, inp().split())
LII = lambda: list(MII())


def main():
    n, k = MII()
    a = sorted(LII())

    print(k + sum(a[:n-k]))


if __name__ == "__main__":
    main()
