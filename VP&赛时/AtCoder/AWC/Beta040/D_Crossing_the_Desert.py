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
    n, G, S = MII()

    t = []
    for _ in range(n):
        p, r = MII()
        t.append((p, r))
    
    t.sort()
    t.append((G, 0))  #! 将终点视为油量为0的加油站

    hq = []

    cnt = 0
    cur = 0
    cur_fuel = S
    for p, r in t:
        dist = p - cur
        
        while cur_fuel < dist:
            if not hq:
                print(-1)
                return
            cur_fuel += -heappop(hq)
            cnt += 1
        
        cur_fuel -= dist
        cur = p
        heappush(hq, -r)
    
    print(cnt)

if __name__ == "__main__":
    main()
