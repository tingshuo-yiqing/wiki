import math
from typing import List, Callable

class SparseTable:
    """
    ST表(Sparse Table)模板
    支持O(nlogn)预处理, O(1)查询区间最值
    """
    
    def __init__(self, arr: List[int], op: Callable[[int, int], int] = min):
        """
        初始化ST表
        :param arr: 输入数组
        :param op: 操作函数,默认为min(也可以是max等满足可重复贡献的操作)
        """
        self.n = len(arr)
        self.op = op
        
        # 计算log值,log_table[i]表示log2(i)向下取整
        self.log_table = [0] * (self.n + 1)
        for i in range(2, self.n + 1):
            self.log_table[i] = self.log_table[i // 2] + 1
        
        # st[i][j]表示从i开始,长度为2^j的区间的最值
        max_log = self.log_table[self.n] + 1
        self.st = [[0] * max_log for _ in range(self.n)]
        
        # 初始化长度为1的区间
        for i in range(self.n):
            self.st[i][0] = arr[i]
        
        # 动态规划填表
        j = 1
        while (1 << j) <= self.n:
            i = 0
            while i + (1 << j) <= self.n:
                self.st[i][j] = self.op(
                    self.st[i][j - 1],
                    self.st[i + (1 << (j - 1))][j - 1]
                )
                i += 1
            j += 1
    
    def query(self, left: int, right: int) -> int:
        """
        查询区间[left, right]的最值 (闭区间)
        :param left: 左端点(0-indexed)
        :param right: 右端点(0-indexed)
        :return: 区间最值
        """
        length = right - left + 1
        k = self.log_table[length]
        
        # 用两个长度为2^k的区间覆盖[left, right]
        return self.op(
            self.st[left][k],
            self.st[right - (1 << k) + 1][k]
        )


# 使用示例
if __name__ == "__main__":
    # 示例1: 区间最小值查询
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    st_min = SparseTable(arr, min)
    
    print("原数组:", arr)
    print("区间[2, 7]最小值:", st_min.query(2, 7))  # 输出: 1
    print("区间[0, 4]最小值:", st_min.query(0, 4))  # 输出: 1
    print("区间[5, 9]最小值:", st_min.query(5, 9))  # 输出: 2
    
    print("\n" + "="*50 + "\n")
    
    # 示例2: 区间最大值查询
    st_max = SparseTable(arr, max)
    print("区间[2, 7]最大值:", st_max.query(2, 7))  # 输出: 9
    print("区间[0, 4]最大值:", st_max.query(0, 4))  # 输出: 5
    print("区间[5, 9]最大值:", st_max.query(5, 9))  # 输出: 9
    
    print("\n" + "="*50 + "\n")
    
    # 示例3: 自定义操作(GCD)
    import math
    arr2 = [12, 18, 6, 24, 30]
    st_gcd = SparseTable(arr2, math.gcd)
    print("数组:", arr2)
    print("区间[0, 2]的GCD:", st_gcd.query(0, 2))  # 输出: 6
    print("区间[1, 4]的GCD:", st_gcd.query(1, 4))  # 输出: 6