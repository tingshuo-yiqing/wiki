import sys
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def main():
    outs = []
    for _ in range(int(input())):
        s, k, m = map(int, input().split())

        if k >= s:
            if m % k == 0:
                outs.append(s)
            else:
                outs.append(max(0, s - m % k))
        else:
            outs.append(max(0, s - m % k))

    print(*outs, sep='\n')

if __name__ == "__main__":
    main()