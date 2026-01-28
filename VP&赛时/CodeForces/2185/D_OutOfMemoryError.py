import sys

input = lambda: sys.stdin.readline().strip()

def main():
    outs = []

    for _ in range(int(input())):
        n, m, h = map(int, input().split())

        a = list(map(int, input().split()))
        aa = a[::]

        op = []
        for i in range(m):
            b, c = map(int, input().split())
            b -= 1
            
            op.append(b)
            a[b] += c
            if a[b] > h:
                for j in op:
                    a[j] = aa[j]
                op.clear()

        outs.append(a)
    
    for o in outs:
        print(*o)

if __name__ == "__main__":
    main()