import sys
from math import comb
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

MOD = 10 ** 9 + 7

def main():
    n = int(input())

    if n == 1:
        print(0)
        sys.exit(0)
    if n == 2:
        print(2)
        sys.exit(0)
                                                      
    # print((((n * (n - 1)) % MOD) * pow(10, n-2, MOD)) % MOD)  # 含有重复
    print((pow(10, n, MOD ) - (-pow(8, n, MOD) + 2 * pow(9, n, MOD))) % MOD)

if __name__ == "__main__":
    main()