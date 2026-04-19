import sys

Max = lambda x, y: x if x > y else y
Min = lambda x, y: x if x < y else y

inp = lambda: sys.stdin.readline().strip()

II = lambda: int(inp())
MII = lambda: map(int, inp().split())
LII = lambda: list(MII())


def main():
    ans = 0

    for _ in range(II()):
        T, P = inp().split()

        p = int(P)
        if T == "normal":
            ans += p
        else:
            ans += p // 2

    print(ans)

if __name__ == "__main__":
    main()
