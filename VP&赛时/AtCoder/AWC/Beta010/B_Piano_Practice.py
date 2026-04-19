import sys

Min = lambda x, y: x if x < y else y
Max = lambda x, y: x if x > y else y

inp = lambda:sys.stdin.readline().strip()

II = lambda: int(inp())
MII = lambda: map(int, inp().split())
LII = lambda: list(MII())


def main():
    n = II()

    a = LII()

    ans = a[0]
    pre = a[0]

    for x in a[1:]:
        if x > pre:
            ans += x // 2
        else:
            ans += x
        pre = x

    print(ans)


if __name__ == "__main__":
    main()
