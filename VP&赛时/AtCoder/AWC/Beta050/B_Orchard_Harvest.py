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
    n, k = MII()

    T = []
    for _ in range(n):
        A, B = MII()
        if A <= B:
            T.append((A, 1))
        else:
            t = A // B
            r = A % B
            T.append((B, t))
            T.append((r, 1))

    T.sort(key=lambda x: -x[0])

    ans = 0
    for v, c in T:
        if k - c >= 0:
            k -= c
            ans += v * c
        else:
            ans += k * v
            break
    
    print(ans)

if __name__ == "__main__":
    main()
