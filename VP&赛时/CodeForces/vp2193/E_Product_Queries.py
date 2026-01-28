import sys
from math import inf

input = lambda: sys.stdin.readline().strip()

Max = lambda x, y: x if x > y else y
Min = lambda x, y: x if x < y else y


def main():
    outs = []
    for _ in range(int(input())):
        n = int(input())

        a = list(map(int, input().split()))
        a = sorted(list(set(a)))

        dp = [inf] * (n + 1)

        for x in a:
            dp[x] = 1
        
        for i in range(1, n + 1):
            if dp[i] == inf:
                continue
            
            for v in a:
                if v * i > n:
                    break
                dp[v * i] = Min(dp[v * i], dp[i] + 1)
        
        outs.append(' '.join(str(x) if x < inf else '-1' for x in dp[1:]))
    
    print('\n'.join(map(str, outs)))

if __name__ == "__main__":
    main()