input = __import__('sys').stdin.readline

def solution(n, ary):
    st = []
    st_val = dict()
    for i, ele in enumerate(['L', 'S', 'R', 'K']):
        st_val[ele] = i % 2

    cnt = 0
    for ele in ary:
        if ele == 'L' or ele == 'S':
            st.append(st_val[ele])
        elif ele == 'R' or ele == 'K':
            if not st: break
            t = st_val[ele]
            k = st.pop()
            if k != t: break
            cnt += 1
        elif '1'<=ele<='9':
            cnt += 1

    return cnt

print(solution(int(input()), input().rstrip()))
