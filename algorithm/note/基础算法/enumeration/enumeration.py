import sys
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def N_K(s, k):
    """递归求解笛卡尔积时间复杂度为 N^K .  
    返回结果数组
    """
    path = []   
    ans = [] 
    def dfs():
        if len(path) == k:
            ans.append(''.join(path))
            return

        for string in s:  # 递归
            path.append(string)
            dfs()
            path.pop()
    return ans



def main():
    n, k, x = map(int, input().split())

    s = [input() for _ in range(n)]

    ans = N_K(s, k)
    ans.sort()
    print(ans[x-1])
if __name__ == "__main__":
    main()