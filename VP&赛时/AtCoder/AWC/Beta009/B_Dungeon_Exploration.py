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
    n, s, c = MII()

    t = [LII() for _ in range(n)]

    cnt = 0
    for h, p in t:
        if s - h >= 0:
            s -= h
            s += p
        else:
            cnt += 1

    print(cnt * c)

if __name__ == "__main__":
    main()
