import sys
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

def main():
    a, b = map(int, input().split())

    print(gcd(a, b))

if __name__ == "__main__":
    main()