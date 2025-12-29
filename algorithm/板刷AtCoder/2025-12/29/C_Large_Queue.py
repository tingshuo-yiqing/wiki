import sys
from collections import deque
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def main():
    n = int(input())

    q = deque()

    outs = []
    for _ in range(n):
        o = list(map(int, input().split()))

        if o[0] == 1:
            q.append((o[1], o[2]))
        else:
            k = o[1]
            ans = 0
            while q:
                u, v = q.popleft()
                if k - u >= 0:
                    ans += u * v
                    k -= u
                else:
                    ans += k * v
                    q.appendleft((u - k, v))
                    break
            outs.append(ans)
    
    print(*outs, sep='\n')

if __name__ == "__main__":
    main()