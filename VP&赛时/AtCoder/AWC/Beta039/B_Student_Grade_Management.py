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
    n, q, T = MII()

    scores = [[0, 0] for _ in range(n + 1)]

    for _ in range(q):
        i, x = MII()
        scores[i][0] += x
        scores[i][1] += 1
    
    ans = 0
    for x, cnt in scores[1:]:
        if cnt != 0 and x < T * cnt:
            ans += 1

    print(ans)

if __name__ == "__main__":
    main()
