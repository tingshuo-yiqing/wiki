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
    n, s, q = MII()

    a = LII()

    it = sorted([(x, i + 1) for i, x in enumerate(a)])

    nxt = [0] * (n + 1)  #! 函数图对应的 nxt 数组
    
    for i in range(n):
        x, k = it[i]
        if i == 0:
            nxt[k] = it[i + 1][1]
        elif i == n - 1:
            nxt[k] = it[i - 1][1]
        else:
            xl, kl = it[i - 1]
            xr, kr = it[i + 1]

            if abs(x - xl) != abs(x - xr):
                nxt[k] = kl if abs(x - xl) < abs(x - xr) else kr
            else:
                nxt[k] = Min(kl, kr)

    vised = [-1] * (n + 1)
    pos = s
    step = 0
    order = []

    while vised[pos] == -1:
        vised[pos] = step
        order.append(pos)
        pos = nxt[pos]
        step += 1
    
    tail_size = vised[pos]  #! 尾巴的大小，同时也是环的起点
    cycle_size = step - tail_size  #! 环的大小

    ans = 0
    if q < tail_size:
        ans = order[q]
    else:
        ans = order[tail_size + (q - tail_size) % cycle_size]
    
    print(ans)

if __name__ == "__main__":
    main()
