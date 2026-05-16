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
    s = inp()

    d = [0] * (n + k)

    ans = 0
    cur = 0

    for i, x in enumerate(s):
        cur += d[i]
        if (int(x) + cur) % 2 == 0:  #! 翻转条件
            if i + k <= n:
                ans += 1
                cur += 1  #! 相当于 d[l] += 1
                d[i + k] -= 1
            else:
                print(-1)
                return
    
    print(ans)

if __name__ == "__main__":
    main()
