import sys

Max = lambda x, y: x if x > y else y
Min = lambda x, y: x if x < y else y

input_type = 1

if input_type:
    inp = lambda: sys.stdin.readline().strip()

    II = lambda: int(inp())
    MII = lambda: map(int, inp().split())
    LII = lambda: list(MII())

else:
    input_data = sys.stdin.read().split()
    it = iter(input_data)
    
    II = lambda: int(next(it))
    SI = lambda: next(it)
    
    if not input_data:
        sys.exit()

def main():

    def vaild(s):
        st = []
        for c in s:
            if c == ')' and len(st) >= 3:
                if ''.join(st[-3:]) == '(xx':
                    st.pop()
                    st.pop()
                    st.pop()
                    st.append('x')
                    st.append('x')
                else:
                    st.append(')')
            else:
                st.append(c)

        return ''.join(st)
        
    outs = []
    for _ in range(II()):
        A = inp()
        B = inp()

        if A.count('x') != B.count('x'):
            outs.append("No")
            continue

        if A == B:
            outs.append("Yes")
            continue

        outs.append("Yes" if vaild(A) == vaild(B) else "No")
    
    print('\n'.join(outs))

if __name__ == "__main__":
    main()
