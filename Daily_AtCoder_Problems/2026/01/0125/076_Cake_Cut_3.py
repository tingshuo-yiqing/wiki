import sys
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

Max = lambda x, y: x if x > y else y
Min = lambda x, y: x if x < y else y
Inf = 10**19

def main():
    n = int(input())

    a = list(map(int, input().split()))

    s = sum(a)
    if s % 10 != 0:
        print("No")
        sys.exit(0)

    a = a + a
    t = s // 10
    
    win = l = 0
    for r in range(2*n - 1):
        win += a[r]
        
        while win > t:
            win -= a[l]
            l += 1

        if win == t:
            print("Yes")
            sys.exit(0)
    print("No")

if __name__ == "__main__":
    main()