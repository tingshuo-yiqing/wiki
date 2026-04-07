import sys
from collections import deque, defaultdict
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
    n = II()
    a = LII()

    cur = 1
    cnt = defaultdict(int)
    first = defaultdict(int)

    hq = [[-1, -1, 1]]

    ans = 0
    for i, x in enumerate(a):
        # print(hq)
        cnt[x] += 1
        if x not in first:
            first[x] = i + 2
        heappush(hq, [-cnt[x], -first[x], x])

        if cur == x:
            ans += 1
        else:
            t1, t2, z = heappop(hq)
            cur = z
            heappush(hq, [t1, t2, z])

    print(ans)

if __name__ == "__main__":
    main()
