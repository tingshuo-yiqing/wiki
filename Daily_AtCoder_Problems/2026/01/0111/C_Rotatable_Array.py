import sys
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def main():
    n, m = map(int, input().split())

    a = list(range(1, n + 1))

    off = 0

    outs = [] 
    for _ in range(m):
        o = list(map(int, input().split()))

        if o[0] == 1:
            idx = (o[1] + off - 1) % n
            a[idx] = o[2]
        elif o[0] == 2:
            idx = (o[1] + off - 1) % n
            outs.append(a[idx])
        else:
            off = (off + o[1]) % n

    print(*outs, sep='\n')
if __name__ == "__main__":
    main()