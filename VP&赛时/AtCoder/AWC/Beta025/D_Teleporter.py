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

    nxt = [0] * (n + 1)
    for i, x in enumerate(a):
        nxt[i + 1] = x
    
    vised = {}
    pos = 1
    step = 0
    order = []

    while pos not in vised:
        vised[pos] = step
        order.append(pos)
        pos = nxt[pos]
        step += 1
    
    # print(order)
    tail_size = vised[pos]
    cycle_size = step - tail_size

    if k < tail_size:
        ans = order[k]
    else:
        ans = order[tail_size + (k - tail_size) % cycle_size]
    
    print(ans)

if __name__ == "__main__":
    main()
