import sys
from itertools import permutations
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def main():
    n, k = map(int, input().split())

    g = [list(map(int, input().split())) for _ in range(n)]

    cnt = 0
    for p in permutations(range(1, n)):
        su = g[0][p[0]] + g[p[n - 2]][0]  
        
        for j in range(n - 2):
            su += g[p[j]][p[j + 1]]
        
        if su == k:
            cnt += 1
    
    print(cnt)

if __name__ == "__main__":
    main()