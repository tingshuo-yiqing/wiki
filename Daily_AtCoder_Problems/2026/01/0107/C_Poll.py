import sys
from collections import defaultdict
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def main():
    n = int(input())

    cnt = defaultdict(int)

    for _ in range(n):
        cnt[input()] += 1
    
    mx = max(cnt.values())

    ans = []
    for k, v in cnt.items():
        if v == mx:
            ans.append(k)

    print(*sorted(ans), sep='\n')
if __name__ == "__main__":
    main()