import sys
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def main():
    n, s = map(int, input().split())

    cnt = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i + j <= s:
                cnt += 1
    
    print(cnt)

if __name__ == "__main__":
    main()