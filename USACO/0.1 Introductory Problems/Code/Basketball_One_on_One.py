import sys
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

Max = lambda x, y: x if x > y else y
Min = lambda x, y: x if x < y else y
Inf = 10**19

def main():
    s = list(input())

    n = len(s)

    cnt = {'A': 0, 'B': 0}
    for i in range(0, n, 2):
        cnt[s[i]] += int(s[i + 1])
    
    print("A" if cnt['A'] > cnt['B'] else "B")

if __name__ == "__main__":
    main()