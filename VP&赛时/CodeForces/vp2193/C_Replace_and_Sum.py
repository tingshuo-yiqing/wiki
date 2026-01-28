import sys
input = lambda: sys.stdin.readline().strip()

Max = lambda x, y: x if x > y else y
Min = lambda x, y: x if x < y else y
Inf = 10**19

def main():
    outs = []
    for _ in range(int(input())):
        n, q = map(int, input().split())

        a = list(map(int, input().split()))
        b = list(map(int, input().split()))

        for i in range(n):
            if b[i] > a[i]:
                a[i] = b[i]
        for i in range(n - 1, 0, -1):
            if a[i] > a[i - 1]:
                a[i - 1] = a[i]

        a = [0] + a      
        pf = [0] * (n + 1)
        for i in range(1, n + 1):
            pf[i] = pf[i-1] + a[i]
        
        o = []
        for _ in range(q):
            l, r = map(int, input().split())
            o.append(pf[r] - pf[l-1])
        outs.append(o)
    
    for o in outs:
        print(*o)

if __name__ == "__main__":
    main()