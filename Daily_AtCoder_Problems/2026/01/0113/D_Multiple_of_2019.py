import sys
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def main():
    s = list(input())

    n = len(s)

    mul = 0
    k = 1
    divs = [0] * 2019
    for i in range(n-1, -1, -1):
        mul = mul + int(s[i]) * k % 2019  # 后缀积
        divs[mul % 2019] += 1
        k = (k * 10) % 2019
    
    ans = 0
    for i, x in enumerate(divs):
        ans += (x * (x - 1) // 2) if i != 0 else (x * (x + 1) // 2)
    
    print(ans)
    
if __name__ == "__main__":
    main()