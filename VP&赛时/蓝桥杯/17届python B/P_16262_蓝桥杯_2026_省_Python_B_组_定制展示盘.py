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

def main():
    for _ in range(II()):
        n = II()

        def is_prime(num):
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
            return n >= 2

        if n <= 4:
            print(4)
        else:
            if is_prime(n):
                n += 1
            print(n)

        # if n <= 4:
        #     print(4)
        # else:
        #     n += n & 1
        #     print(n)


if __name__ == "__main__":
    main()
