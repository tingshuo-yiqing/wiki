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
    n, q = MII()

    a = [0] * (n + 1)

    outs = []

    for _ in range(q):
        op, x, y, v = MII()
        if op == 1:
            a[x] -= v
            a[y] += v
        elif op == 2:
            cnt = 0
            for i in range(y, v + 1):
                if a[i] > a[x]:
                    cnt += 1
            outs.append(cnt)
        else:
            for i in range(x, y + 1):
                a[i] += v
    
    print(*outs, sep='\n')  

if __name__ == "__main__":
    main()
