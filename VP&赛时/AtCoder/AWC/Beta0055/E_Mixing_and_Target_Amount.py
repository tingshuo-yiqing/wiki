import sys
from collections import defaultdict

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
    n, k = MII()

    if k == 0:
        print("Yes")
        return
    # def get_subsum(ap, ah):
    #     sz = len(ap)
    #     cnt = set()
        
    #     def dfs(idx, cur):
    #         if idx == sz:
    #             cnt.add(cur)
    #             return
    #         dfs(idx + 1, cur)           # 选 0：不选
    #         dfs(idx + 1, cur + ap[idx]) # 选 1：选 p
    #         dfs(idx + 1, cur + ah[idx]) # 选 2：选 h
        
    #     dfs(0, 0)
    #     return cnt

    T = []
    for _ in range(n):
        a, b = MII()
        T.append((0, a, b))

    mid = n // 2
    a1 = T[mid:]
    a2 = T[:mid]

    def get_subsum(ap):
        sz = len(ap)
        cnt = defaultdict(int)
        for i in range(3 ** sz):
            s = 0
            t = i
            for j in range(sz):
                s += ap[j][t % 3]
                t //= 3
            cnt[s] = 1
        return cnt

    cnt1 = get_subsum(a1)
    cnt2 = get_subsum(a2)

    for v in cnt2:
        if k - v in cnt1:
            print("Yes")
            return

    print("No")

if __name__ == "__main__":
    main()
