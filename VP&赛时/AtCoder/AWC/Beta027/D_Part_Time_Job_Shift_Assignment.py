import sys
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
    n, m = MII()

    hq = []
    t = []
    for _ in range(n):
        h, s = MII()
        t.append((h, s))
    t.sort()

    a = sorted(LII())

    ans = 0
    j = 0
    for x in a:
        while j < n and t[j][0] <= x:
            heappush(hq, -t[j][1])
            j += 1
        
        #! 题目要求每个人第一个上岗，当前没有选择时直接退出
        if not hq:
            ans = -1
            break
        ans += -heappop(hq)
    
    print(ans)

if __name__ == "__main__":
    main()
