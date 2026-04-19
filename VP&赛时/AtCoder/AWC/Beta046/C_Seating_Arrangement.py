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
    s = LII()

    ans = 0
    for i in range(n):
        if s[i] == 0:
            l, r = i - 1, i + 1
            cnt = 0
            while l >= 0 and s[l] == 1:
                cnt += 1
                l -= 1
            while r < n and s[r] == 1:
                cnt += 1
                r += 1
            if cnt < 2:
                s[i] = 1
                ans += 1
    # print(*s)
    print(ans)
    
if __name__ == "__main__":
    main()
