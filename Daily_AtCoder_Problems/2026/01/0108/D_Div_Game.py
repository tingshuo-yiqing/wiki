import sys
from collections import defaultdict
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def main():
    n = int(input())

    divs = defaultdict(int)

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            while n % i == 0:
                divs[i] += 1
                n //= i
    if n != 1:
        divs[n] = 1

    ans = 0
    for v in divs.values():
        cur = 1
        cnt = 0
        while v >= cur:
            v -= cur
            cur += 1
            cnt += 1
        ans += cnt
    
    print(ans)

if __name__ == "__main__":
    main()