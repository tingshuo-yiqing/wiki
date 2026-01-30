import sys
from collections import deque
input = lambda: sys.stdin.readline().strip()

Max = lambda x, y: x if x > y else y
Min = lambda x, y: x if x < y else y


def main():
    outs = []
    for _ in range(int(input())):
        n = int(input())

        a = list(map(int, input().split()))
        a.sort()

        i = 0
        for j in range(1, n):
            if a[j] != a[i]:
                i += 1
                a[i] = a[j]
        a = a[:i + 1]

        d = deque(a)

        vised = [-1] * (n + 1)
        for x in a:
            vised[x] = 1
        
        while d:
            u = d.popleft()
            for v in a:
                if u * v > n:
                    break
                cur = u * v
                if vised[cur] == -1:
                    vised[cur] = vised[u] + 1
                    d.append(cur)
                    
        outs.append(' '.join(str(x) for x in vised[1:]))
    
    print('\n'.join(map(str, outs)))

if __name__ == "__main__":
    main()