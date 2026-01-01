import sys
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def trans(x, n, base):
    """x -> 10 -> base"""
    num = int(n, x)   # 将 x 转化为 10 进制
    if num == 0: return '0'
    
    # 进制转换字符映射表
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = []

    while num:
        # divmod 返回 (num // base, num % base)
        num, r = divmod(num, base)
        res.append(digits[r])

    return ''.join(res[::-1])  # 返回逆序字符串

def fast_convert(n, b):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return (fast_convert(n // b, b) + digits[n % b]) if n else ""

def replace(s):
    s = list(s)

    for i in range(len(s)):
        if s[i] == '8':
            s[i] = '5'
    return ''.join(s)

def main():
    n, k = map(int, input().split())

    n = str(n)

    for _ in range(k):
        n = trans(8, n, 9)
        n = replace(n)
    
    print(n)

if __name__ == "__main__":
    main()