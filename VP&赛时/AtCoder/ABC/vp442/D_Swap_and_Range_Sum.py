import sys
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

Max = lambda x, y: x if x > y else y
Min = lambda x, y: x if x < y else y
Inf = 10**19

def main():
    n, q = map(int, input().split())

    a = [0] + list(map(int, input().split()))
    
    pf = [0] * (n + 1)
    for i in range(1, n+1):
        pf[i] = pf[i-1] + a[i]

    outs = []
    for _ in range(q):
        o = list(map(int, input().split()))
        op = o[0]
        if op == 1:
            i = o[1]
            pf[i] += (a[i+1] - a[i])
            a[i], a[i+1] = a[i+1], a[i]
        else:
            l, r = o[1:]
            outs.append(pf[r] - pf[l-1])
    
    print(*outs, sep='\n')

if __name__ == "__main__":
    main()