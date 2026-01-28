import sys
import os
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

if os.path.exists('teleport.in'):
    sys.stdin = open('teleport.in', 'r')
    sys.stdout = open('teleport.out', 'w')

Max = lambda x, y: x if x > y else y
Min = lambda x, y: x if x < y else y
Inf = 10**19

def main():
    a, b, c, d = map(int, input().split())

    t1 = abs(a - b)
    t2 = abs(a - c) + abs(d - b)
    t3 = abs(a - d) + abs(c - b)
    
    print(min(t1, t2, t3))    

if __name__ == "__main__":
    main()