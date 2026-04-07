import sys
from collections import deque

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
    for _ in range(II()):
        n, k = MII()

        a = LII()

        t = a.index(n)

        dq =  deque(a)

        idx = 0
        for _ in range(Min(k, t)):
            if dq[idx + 1] > dq[idx]:
                dq.rotate(-1)
            else:
                dq.append(dq[idx+1])
                dq[idx+1] = dq[idx]
                idx += 1
        
        cnt = Max(k - t, 0) % (n - 1)

        if cnt > 0:
            temp = deque()
            for i in range(n-1):
                temp.append(dq[idx+i+1])
            for _ in range(cnt):
                temp.rotate(-1)

            print(n, end=' ')
            print(*temp)
        else:
            for i in range(n):
                print(dq[idx+i], end=' ')
            print()

if __name__ == "__main__":
    main()
