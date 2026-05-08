import sys

Max = lambda x, y: x if x > y else y
Min = lambda x, y: x if x < y else y

input_type = 1

if input_type:
    inp = lambda: sys.stdin.readline().strip()

    II = lambda: int(inp())
    MII = lambda: map(int, inp().split())
    LII = lambda: list(MII())

else:
    input_data = sys.stdin.read().split()
    it = iter(input_data)
    
    II = lambda: int(next(it))
    SI = lambda: next(it)
    
    if not input_data:
        sys.exit()

def main():
    n, m, k = MII()
    T = LII()

    b = []
    for i in range(n):
        s = LII()

        if all(x >= y for x, y in zip(s, T)):
            b.append((i + 1, sum(s)))

    if len(b) <= k:
        for i, j in b:
            print(i)
    else:
        d = b[:]
        b.sort(key=lambda x: -x[1])
        # print(*b)

        std = b[k-1][1]

        for i, j in d:
            if j >= std:
                print(i)

if __name__ == "__main__":
    main()
