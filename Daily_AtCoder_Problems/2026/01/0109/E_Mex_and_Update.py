import sys
import heapq
from collections import defaultdict
input = lambda: sys.stdin.readline().strip()

class MexManager:
    def __init__(self, arr):
        n = len(arr)
        # self.freq = [0] * (n + 2)
        self.freq = defaultdict(int)
        self.arr = list(arr)
        
        # 记录哪些数字 [0, n+1] 没在数组里
        missing_elements = []
        
        # 统计初始频率
        for x in self.arr:
            self.freq[x] += 1
        
        # 初始没出现的数字入堆
        for i in range(n + 2):
            if self.freq[i] == 0:
                heapq.heappush(missing_elements, i)
        
        self.missing_elements = missing_elements

    def get_mex(self):
        # 堆顶不一定准确（可能后来被加入了），需要“延迟删除”
        while self.missing_elements and self.freq[self.missing_elements[0]] > 0:
            heapq.heappop(self.missing_elements)
        return self.missing_elements[0]

    def update(self, idx, new_val):
        old_val = self.arr[idx]
        n = len(self.arr)
        
        if old_val == new_val:
            return

        # 处理旧值
        self.freq[old_val] -= 1
        if self.freq[old_val] == 0:
            heapq.heappush(self.missing_elements, old_val)
        
        # 处理新值
        self.arr[idx] = new_val
        self.freq[new_val] += 1


def main():
    n, q = map(int, input().split())

    nums = list(map(int, input().split()))

    M = MexManager(nums)

    outs = []
    for _ in range(q):
        i, x = map(int, input().split())
        M.update(i - 1, x)
        outs.append(M.get_mex())

    print(*outs, sep='\n')

if __name__ == "__main__":
    main()