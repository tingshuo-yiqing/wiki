import sys
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def counter(S, N):
    """ 计算在[1, N]下可以组合成S的组合数 """
    return max(0, min(S - 1, min(S - 1, 2 * N - S + 1)))

def main():
    n = int(input())
    k = int(input())

    ans = 0
    for i in range(2, int(k ** 0.5) + 1):
        if k % i == 0:
            j = k // i
            
            ii = counter(i, n)
            jj = counter(j, n)

            ans += ii * jj
            if i != j:
                ans += ii * jj
    
    
    print(ans)

if __name__ == "__main__":
    main()