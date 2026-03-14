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
    a = LII()
    b = LII()

    b.sort()

    j = 0
    ans = cnt = 0
    for i in range(n):
        if j < m and i + 1 == b[j]:
            if a[i] < k:
                cnt += 1
                ans += a[i]
            j += 1
    
    print(cnt, ans)

if __name__ == "__main__":
    main()
