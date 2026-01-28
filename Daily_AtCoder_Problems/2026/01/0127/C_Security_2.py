import sys
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

Max = lambda x, y: x if x > y else y
Min = lambda x, y: x if x < y else y
Inf = 10**19

def main():
    s = [int(i) for i in input()]
    n = len(s)

    d = 0
    ans = 0
    for i in range(n-1, -1, -1):  
        ans += (s[i] - d) % 10  
        d += s[i] - d  # s[i] - d为当前位达到目标的操作次数
    
    print(ans + n)

if __name__ == "__main__":
    main()