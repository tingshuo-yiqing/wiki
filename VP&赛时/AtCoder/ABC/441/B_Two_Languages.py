import sys
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def main():
    n, m = map(int, input().split())
    s = input()
    t = input()
    
    q = int(input())
    for _ in range(q):
        a = list(input())

        f1 = f2 = False
        if all(c in t for c in a):
            f1 = True
        if all(c in s for c in a):
            f2 = True

        if f1 and f2:
            print("Unknown")
        elif f1:
            print("Aoki")
        else:
            print("Takahashi")

if __name__ == "__main__":
    main()