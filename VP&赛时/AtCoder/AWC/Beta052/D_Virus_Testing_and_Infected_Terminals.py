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
    n, m = MII()

    state = []
    for _ in range(m):
        state.append(LII())
    
    res = 10 ** 9
    for i in range(1 << n):
        f = True
        for g in state:
            cnt = 0
            infect = g[-1]
            for x in g[1:-1]:
                x -= 1
                if (i >> x) & 1:
                    cnt += 1
            if infect == 1 and cnt == 0:
                f = False
                break
            if  infect == 0 and cnt != 0:
                f = False
                break
        if f:
            res = Min(res, i.bit_count())
    
    print(res)

if __name__ == "__main__":
    main()
