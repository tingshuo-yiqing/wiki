import sys
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def main():
    n = int(input())

    nums = list(map(int, input().split()))

    st = []
    
    for x in nums:
        cur = x
        while st and st[-1] == cur:  # 维护一个连锁反应
            st.pop()
            cur += 1  # 不断的更新
        st.append(cur)

    # print(st)
    print(len(st))

if __name__ == "__main__":
    main()