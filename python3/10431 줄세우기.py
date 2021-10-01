input = __import__('sys').stdin.readline

tc = int(input())
for _ in range(tc):
    n, *ary = map(int, input().split())
    ans = 0
    st = []

    for i, ele in enumerate(ary):
        if not st or st[-1] < ele:
            st.append(ele)
            continue
        cnt = i - 1
        while cnt > 0 and st[cnt - 1] > ele:
            cnt -= 1
        ans += i - cnt
        st.insert(cnt, ele)
    print(n, ans)