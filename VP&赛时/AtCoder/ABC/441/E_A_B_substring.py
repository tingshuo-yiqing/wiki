def solve():
    N = int(input())
    S = input().strip()
    
    # D 的范围是 [-N, N]，偏移 N 后为 [0, 2N]
    counter = [0] * (2 * N + 1)
    D = N  # 初始 D_0 = 0，偏移后为 N
    counter[D] = 1
    
    sum_less = 0
    ans = 0
    
    for c in S:
        if c == 'A':
            sum_less += counter[D]
            D += 1
        elif c == 'B':
            D -= 1
            sum_less -= counter[D]
        # C 不改变 D
        
        counter[D] += 1
        ans += sum_less
    
    print(ans)

if __name__ == "__main__":
    solve()