import sys
input = lambda: sys.stdin.readline().strip()

Max = lambda x, y: x if x > y else y
Inf = 10**19

def main():
    outs = []
    for _ in range(int(input())):
        n = int(input())

        a = sorted(list(map(int, input().split())), reverse=True)
        b = list(map(int, input().split()))

        ans = h =  0
        s = 0
        for i, x in enumerate(a, start=1):
            while h < n and i >= s + b[h]:
                s += b[h]
                h += 1
            ans = Max(ans, x * h)

        outs.append(ans)
    
    print(*outs, sep='\n')

if __name__ == "__main__":
    main()