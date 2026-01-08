import sys
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

MOD = 998244353

def main():
    a, b, c = map(lambda x: int(x) % MOD, input().split())

    sa = a * (a + 1) // 2
    sb = b * (b + 1) // 2
    sc = c * (c + 1) // 2
    
    print((sa % MOD * sb % MOD) % MOD * sc % MOD)
    
if __name__ == "__main__":
    main()