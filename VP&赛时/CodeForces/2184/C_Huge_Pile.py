import sys
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def main():
    outs = []
    for _ in range(int(input())):
        n, k = map(int, input().split())

        ans = -1
        for i in range(32):
            p = 1 << i
            a = n // p
            b = (n + p - 1) // p

            if k == a or k == b:
                ans = i
                break

        outs.append(ans)

    print(*outs, sep='\n')

if __name__ == "__main__":
    main()