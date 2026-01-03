import sys
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def main():
    st = set()

    outs = []
    for i in range(int(input())):
        s = input()
        if s not in st:
            outs.append(i + 1)
            st.add(s)
        
    print(*outs, sep='\n')
if __name__ == "__main__":
    main()