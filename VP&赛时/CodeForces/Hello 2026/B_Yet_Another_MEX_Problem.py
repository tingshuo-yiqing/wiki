import sys

input = lambda: sys.stdin.readline().strip()

# def mex(arr):
#     nums = set(arr)
    
#     ret = 0
#     while ret in nums:
#         ret += 1

#     return ret

def mex(arr):
    n = len(arr)
    vised = [False] * (n + 1)

    for x in arr:
        vised[x] = True

    ret = 0
    while vised[ret]:
        ret += 1
    return ret

def main():
    outs = []

    for _ in range(int(input())):
        n, k = map(int, input().split())

        nums = list(map(int, input().split()))

        outs.append(min(k - 1, mex(nums)))  
    
    print(*outs, sep='\n')

if __name__ == "__main__":
    main()