import sys
from collections import Counter
from heapq import heapify, heappop, heappush

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
    a = LII()
    s = list(set(a))

    cnt = Counter(a)

    outs = []
    heapify(s)
    for _ in range(q):
        t = II()
        b = LII()

        for x in b:
            cnt[a[x - 1]] -= 1
        
        pre = []
        while True:
            cur = heappop(s)
            pre.append(cur)
            if cnt[cur] != 0:
                outs.append(cur)
                break                
        for x in pre:
            heappush(s, x)

        for x in b:
            cnt[a[x - 1]] += 1
    
    print(*outs, sep='\n')

if __name__ == "__main__":
    main()
