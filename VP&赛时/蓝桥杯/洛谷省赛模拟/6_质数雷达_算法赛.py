import sys

Max = lambda x, y: x if x > y else y
Min = lambda x, y: x if x < y else y

input_type = 1

if input_type:
    inp = lambda: sys.stdin.readline().strip()

    II = lambda: int(inp())
    MII = lambda: map(int, inp().split())
    LII = lambda: list(MII())

else:
    input_data = sys.stdin.read().split()
    it = iter(input_data)
    
    II = lambda: int(next(it))
    SI = lambda: next(it)
    
    if not input_data:
        sys.exit()

def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return n >= 2

def main():
    a, c = MII()

    cnt = 0
    for x in range(a, 10 ** 9 + 1):
        if x % 2 == 0:
            continue
        if is_prime(x):
            cnt += 1
        
        if cnt == c:
            print(x)
            break

if __name__ == "__main__":
    main()
