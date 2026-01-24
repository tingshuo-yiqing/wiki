import sys
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def is_primes(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return n >= 2

def main():
    n = int(input())

    if is_primes(n):
        print(0)
        sys.exit(0)
    
    cnt = 0
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            while n % x == 0:
                cnt += 1
                n //= x
    cnt += (n != 1)
    
    # print((cnt - 1).bit_length())
    ans = 0
    while (1 << ans) < cnt:
        ans += 1
    print(ans)
if __name__ == "__main__":
    main()