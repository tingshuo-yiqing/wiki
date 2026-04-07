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

MOD = 998244353

def main():
    outs = []

    for _ in range(II()):
        x, y = MII()

        if x <= y:
            outs.append(1)
            continue

        add = y + 1
        cur = 0
        for _ in range(x - y):  # 这个for循环应该怎么取模
            add = (add + cur) % MOD
            cur = add
            
        outs.append(cur % MOD)
    
    print(*outs, sep='\n')

if __name__ == "__main__":
    main()
