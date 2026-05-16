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
    N, L, K, Y = MII()

    a = LII()

    T = [x for x in a if x > L]
    T.sort()

    ans = 0
    for i in range(Min(len(T), K), len(T)):
        if T[i] - Y > L:
            ans += 1

    print(Min(K, len(T)) + ans)

if __name__ == "__main__":
    main()
