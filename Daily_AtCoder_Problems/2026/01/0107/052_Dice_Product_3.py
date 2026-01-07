import sys
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

MOD = 10 ** 9 + 7

def main():
    n = int(input())

    dice  = []
    for i in range(n):
        dice.append(sum(list(map(int, input().split()))))
    
    ans = 1
    for x in dice:
        ans = (ans * x) % MOD

    print(ans)

if __name__ == "__main__":
    main()