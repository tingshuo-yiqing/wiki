import sys
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def main():
    n, m = map(int, input().split())

    conditions = []
    for _ in range(m):
        a, b = map(int, input().split())
        conditions.append((a, b))
    
    k = int(input())
    
    behave = []
    for _ in range(k):
        a, b = map(int, input().split())
        behave.append((a, b))

    ans = 0
    for i in range(1 << k):
        dish = [0] * (n + 1)
        for j in range(k):
            dish[behave[j][(i >> j) & 1]] += 1

        cnt = 0
        for a, b in conditions:
            if dish[a] and dish[b]:
                cnt += 1

        ans = max(ans, cnt)
    
    print(ans)

if __name__ == "__main__":
    main()