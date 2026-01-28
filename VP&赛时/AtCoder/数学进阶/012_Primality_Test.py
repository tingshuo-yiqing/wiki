import sys
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return n >= 2

def main():
    n = int(input())

    print("Yes" if is_prime(n) else "No")

if __name__ == "__main__":
    main()