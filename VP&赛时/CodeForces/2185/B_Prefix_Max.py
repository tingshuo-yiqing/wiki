import sys
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def main():
    outs = []
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int, input().split()))

        mx = max(a)
        outs.append(mx * n)
    
    print(*outs, sep='\n')
if __name__ == "__main__":
    main()