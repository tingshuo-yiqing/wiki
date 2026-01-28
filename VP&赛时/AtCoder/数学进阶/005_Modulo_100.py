import sys
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def main():
    n = int(input())

    a = list(map(int, input().split()))

    MOD = 100

    su = 0
    for x in a:
        su = (su + x) % MOD

    print(su) 

if __name__ == "__main__":
    main()