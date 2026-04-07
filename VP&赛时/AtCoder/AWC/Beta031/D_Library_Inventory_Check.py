import sys
from bisect import bisect_left

def solve():
    # 使用快速输入
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    ptr = 0
    N = int(input_data[ptr]); ptr += 1
    M = int(input_data[ptr]); ptr += 1
    
    # L_i: 第 i 天最多检查的书
    L = []
    for _ in range(N):
        L.append(int(input_data[ptr]))
        ptr += 1
        
    # R_j: 第 j 本书至少检查的次数
    R = []
    for _ in range(M):
        R.append(int(input_data[ptr]))
        ptr += 1
    
    # 1. 对 R 从大到小排序，计算前缀和
    R.sort(reverse=True)
    prefix_sum_R = [0] * (M + 1)
    for i in range(M):
        prefix_sum_R[i+1] = prefix_sum_R[i] + R[i]
        
    # 2. 对 L 从小到大排序，计算前缀和以便二分计算 sum(min(k, L_i))
    L.sort()
    prefix_sum_L = [0] * (N + 1)
    for i in range(N):
        prefix_sum_L[i+1] = prefix_sum_L[i] + L[i]
        
    # 3. 判定条件：对每一个 k (1 到 M)，检查前 k 本书的需求是否能被覆盖
    # 判定式: sum(R_j for j=1..k) <= sum(min(k, L_i) for i=1..N)
    
    is_possible = True
    for k in range(1, M + 1):
        # 需求量：前 k 大的 R 之和
        demand = prefix_sum_R[k]
        
        # 供应量：sum(min(k, L_i))
        # 找到 L 中第一个大于等于 k 的位置 idx
        idx = bisect_left(L, k)
        # L[0...idx-1] 都小于 k，贡献是它们本身的和
        # L[idx...N-1] 都大于等于 k，每个贡献都是 k
        supply = prefix_sum_L[idx] + (N - idx) * k
        
        if demand > supply:
            is_possible = False
            break
            
    if is_possible:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    solve()