import sys
from math import inf
if 1:
    inp = lambda: sys.stdin.readline().strip()

    II = lambda: int(inp())
    MII = lambda: map(int, inp().split())
    LII = lambda: list(MII())

    Max = lambda x, y: x if x > y else y
    Min = lambda x, y: x if x < y else y

def main():
    n = II()
    a = LII()
    
    state = 0
    for i in range(n - 1):
        if a[i] == a[i + 1]:
            if state == 2:  # 平: 只能从0和1过来，且变为1
                print("NO")
                sys.exit(0)
            state = 1

        if a[i] < a[i + 1]: # 递增: 只能从0开始
            if state != 0:
                print("NO")
                sys.exit(0)
        
        if a[i] > a[i + 1]: # 递减: 变为2
            state = 2
    
    print("YES")

if __name__ == "__main__":
    main()