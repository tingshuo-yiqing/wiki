import sys
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

Max = lambda x, y: x if x > y else y
Min = lambda x, y: x if x < y else y
Inf = 10**19

def main():
    s = input()

    ans = 0
    for i in s:
        if i in 'ij':
            ans += 1
    print(ans)

if __name__ == "__main__":
    main()