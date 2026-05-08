import sys

def solve():
    # 快速 I/O 读取所有数据
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    idx = 1
    
    out = []
    for _ in range(t):
        n = int(input_data[idx])
        idx += 1
        
        a =[]
        for _ in range(n):
            a.append(int(input_data[idx]))
            idx += 1
            
        a.sort()
        
        # 定义 check 函数：判断是否能凑齐 0 到 M-1
        def check(M):
            present =[False] * M
            rem =[]  # 记录所有"变身材料"
            
            # 第一步：锁定所有的原配
            for x in a:
                if x < M and not present[x]:
                    present[x] = True
                else:
                    rem.append(x)  # 重复的数字，或者 >= M 的数字，统统当材料
                    
            # 第二步：找出还没被覆盖的缺口
            unmatched = [i for i in range(M) if not present[i]]
            
            # 材料数量不够填补缺口，直接失败
            if len(unmatched) > len(rem):
                return False
                
            # 第三步：大数字去填大缺口
            # rem 本身已经是升序的，取最后 len(unmatched) 个最大的材料
            offset = len(rem) - len(unmatched)
            for i in range(len(unmatched)):
                target = unmatched[i]
                used_val = rem[offset + i]
                if used_val < 2 * target + 1:
                    return False
            
            return True

        # 二分查找最大的 MEX
        left, right = 0, n + 1
        ans = 0
        
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                ans = mid
                left = mid + 1    # 还能更大，往右搜
            else:
                right = mid - 1   # 不行，往左搜
                
        out.append(str(ans))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()