import sys
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

Max = lambda x, y: x if x > y else y
Min = lambda x, y: x if x < y else y
Inf = 10**19

def main():
    n = int(input())

    def is_prime(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return n >= 2
    
    while not is_prime(n):
        n += 1
    
    print(n)

if __name__ == "__main__":
    main()