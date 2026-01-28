import sys
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

Max = lambda x, y: x if x > y else y
Min = lambda x, y: x if x < y else y
Inf = 10**19

def main():
    outs = []
    for _ in range(int(input())):
        n, s, x = map(int, input().split())

        a = list(map(int, input().split()))

        t = s - sum(a)

        if t >= 0 and t % x == 0:
            print("YES") 
        else:
            print("NO")

if __name__ == "__main__":
    main()