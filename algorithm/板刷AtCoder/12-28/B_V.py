import sys
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

"""观察样例可知，连续的部分为一个连通块，逆序输出联通快到ans"""

def main():
    n, m = map(int, input().split())

    a = list(map(int, input().split()))

    connect = [False] * (n - 1) # 判断相邻两个元素是否符合一定条件
    for i in a:
        connect[i - 1] = True  # 判断相邻两个数的连通性
    ans = []
    
    i = 0
    while i < n:
        j = i
        while j < n - 1 and connect[j]:  
            j += 1
        ans += list(range(j + 1, i, -1))
        i = j + 1
    print(*ans)
if __name__ == "__main__":
    main()