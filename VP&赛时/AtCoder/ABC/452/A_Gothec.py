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
    n, m = MII()

    if n == m == 3:
        print("Yes")
    elif n == 1 and m == 7:
        print("Yes")
    elif n == 5 and m == 5:
        print("Yes")
    elif n == 7 and m == 7:
        print("Yes")
    elif n == 9 and m == 9:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
