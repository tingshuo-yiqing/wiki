import sys
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

Max = lambda x, y: x if x > y else y
Min = lambda x, y: x if x < y else y
Inf = 10**19

def main():
    outs = []
    for _ in range(int(input())):
        n, m = map(int, input().split())

        outs.append(m + n + 1)
    
    print(*outs,sep='\n')

if __name__ == "__main__":
    main()