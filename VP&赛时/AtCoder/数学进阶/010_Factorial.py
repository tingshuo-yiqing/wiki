import sys
from math import factorial
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def main():
    print(factorial(int(input())))    

if __name__ == "__main__":
    main()