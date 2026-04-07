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
        n, m = MII()
        nums = [int(i) for i in inp()]

        op = inp()

        idx = 0
        for i in range(m):
            if op[i] == 'L':
                idx -= 1
                idx = Max(0, idx)
            elif op[i] == 'R':
                idx += 1
                idx = Min(n-1, idx)
            elif op[i] == 'U':
                nums[idx] = (nums[idx] + 1) % 10 
            elif op[i] == 'D':
                nums[idx] = (nums[idx] - 1) % 10 

        print(''.join(map(str, nums)))

if __name__ == "__main__":
    main()
