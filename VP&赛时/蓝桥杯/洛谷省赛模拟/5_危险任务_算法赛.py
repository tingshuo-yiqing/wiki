import sys
from collections import deque, defaultdict

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
    a, b, c = MII()

    dq = deque([a])


    ans = 0
    while dq:
        ans += 1

        for _ in range(len(dq)):
            u = dq.popleft()

            for i in range(1, 3):
                v = u + i
                if v == b:
                    print(ans)
                    return 1
                if v % c != 0:
                    dq.append(v)

if __name__ == "__main__":
    main()
