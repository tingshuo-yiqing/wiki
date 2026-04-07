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
    target = 2025

    for i in range(1, 1000):
        target -= 5

        target -= 15 if i & 1 else 2

        m = i % 3
        if m == 1:
            target -= 2
        elif m == 2:
            target -= 10
        else:
            target -= 7
        
        if target <= 0:
            print(i)
            break

if __name__ == "__main__":
    main()
