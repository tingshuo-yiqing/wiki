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
    n, m = MII()

    T = [[]]
    for _ in range(n):
        c, p = MII()
        T.append([c, p])

    cnt = value = 0
    for _ in range(m):
        idx = II()

        if T[idx][1] >= 1:
            T[idx][1] -= 1
            value += T[idx][0]

    print(value)

if __name__ == "__main__":
    main()
    
