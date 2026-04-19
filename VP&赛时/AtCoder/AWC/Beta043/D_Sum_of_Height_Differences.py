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
    n = II()
    a = sorted(LII())
    
    ans = 0
    cur = sum(a)
    for i in range(n):
        cur -= a[i]
        ans += cur - a[i] * (n - i - 1)
    
    print(ans)

if __name__ == "__main__":
    main()
