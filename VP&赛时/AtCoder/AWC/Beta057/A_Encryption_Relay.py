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
    a = LII()

    ans = k ^ a[0]
    for i in range(1, n -1):
        if a[i - 1] == a[i + 1] and a[i - 1] != a[i]:
            continue
        else:
            ans ^= a[i]
    if n > 1:
        ans ^= a[-1]
        
    print(ans)

if __name__ == "__main__":
    main()
