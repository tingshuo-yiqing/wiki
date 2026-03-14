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
    n, m, k = MII()

    d = [deque()]
    for _ in range(n):
        t = list(inp())
        d.append(deque(t))

    outs = []
    st = []
    for x in LII()[:-1]:
        if x == 0:
            if st:
                outs.append(st.pop())
        else:
            if d[x]:
                if len(st) == k:
                    outs.append(st.pop())
                st.append(d[x].popleft())
            
    print(''.join(outs))

if __name__ == "__main__":
    main()
